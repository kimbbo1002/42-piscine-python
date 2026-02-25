from typing import Any, List, Optional, Dict, Union
from abc import ABC, abstractmethod


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        """Initializing data"""
        self.id = stream_id
        self.processed_count = 0
        self.filtered_count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data"""
        pass

    def filter_data(
            self, data_batch: List[Any],
            criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter data based on criteria"""
        return [d for d in data_batch if str(criteria) in str(d)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics"""
        return {"Stream ID": {self.id}}


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        """Initializing data"""
        super().__init__(stream_id)
        self.type = "Environmental Data"
        self.avg = 0.0

    def filter_data(
            self, data_batch: list[Any],
            criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter data based on criteria"""
        filtered = (
            [data for data in data_batch
             if not criteria or criteria in data]
        )
        self.filtered_count = len(data_batch) - len(filtered)
        return filtered

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data for Sensor Stream"""
        valid_data = []
        for data in data_batch:
            if isinstance(data, str) and ':' in data:
                parts = data.split(':')
                try:
                    float(parts[1])
                    valid_data.append(data)
                except Exception:
                    continue
        values = [float(data.split(':')[1]) for data in valid_data]
        count = len(values)
        self.avg = sum(values) / count if count > 0 else 0.0
        self.processed_count = count
        return f"Processing sensor batch: {data_batch}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics"""
        return {
            "data filtered": self.filtered_count,
            "data processed": self.processed_count,
            "avg_tmp": self.avg
        }


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        """Initializing data"""
        super().__init__(stream_id)
        self.type = "Financial Data"
        self.net_flow = 0.0

    def filter_data(
            self, data_batch: list[Any],
            criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter data based on criteria"""
        filtered = (
            [data for data in data_batch
             if not criteria or criteria in data]
        )
        self.filtered_count = len(data_batch) - len(filtered)
        return filtered

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data for Transaction Stream"""
        total = 0.0
        valid_data = []
        for data in data_batch:
            if isinstance(data, str) and ':' in data:
                parts = data.split(':')
                try:
                    val = float(parts[1])
                    if parts[0] in ["buy", "sell"]:
                        valid_data.append(val)
                        total += val if parts[0] == "buy" else -val
                except Exception:
                    continue
        self.net_flow = total
        self.processed_count = len(valid_data)
        return f"Processing transaction batch: {data_batch}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics"""
        return {
            "data filtered": self.filtered_count,
            "data processed": self.processed_count,
            "net_flow": self.net_flow
        }


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        """Initializing data"""
        super().__init__(stream_id)
        self.type = "System Events"
        self.error_count = 0

    def filter_data(
            self, data_batch: list[Any],
            criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter data based on criteria"""
        filtered = (
            [data for data in data_batch
             if not criteria or criteria in data]
        )
        self.filtered_count = len(data_batch) - len(filtered)
        return filtered

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data for Event Stream"""
        valid_data = []
        logs = ["login", "logout", "error"]
        error = 0
        for data in data_batch:
            if isinstance(data, str) and data in logs:
                valid_data.append(data)
                if data == "error":
                    error += 1
        self.processed_count = len(valid_data)
        self.error_count = error
        return f"Processing event batch: {data_batch}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics"""
        return {
            "data filtered": self.filtered_count,
            "data processed": self.processed_count,
            "error_count": self.error_count
        }


class StreamProcessor:
    def __init__(self) -> None:
        """Initializing Stream Processor"""
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        if isinstance(stream, DataStream):
            self.streams.append(stream)
        else:
            print("Error: Cannot add stream")


def stream_tester() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSEM ===\n")

    print("Initializing Sensor Stream...")
    s1 = SensorStream("SENSOR_001")
    d1 = ["Grenoble(Rhone):22.5", "Lyon(Rhone):25", "Toulouse(Occitane):29"]
    print(
        f"Stream ID: {s1.id}, Type: {s1.type}\n"
        f"{s1.process_batch(s1.filter_data(d1, None))}"
    )
    s1_stats = s1.get_stats()
    print("Sensor analysis:")
    for name, info in s1_stats.items():
        print(f"   - {name}: {info}")

    print("\nInitializing Transaction Stream...")
    s2 = TransactionStream("TRANS_001")
    d2 = ["buy:100", "sell:150", "buy:75"]
    print(
        f"Stream ID: {s2.id}, Type: {s2.type}\n"
        f"{s2.process_batch(s2.filter_data(d2, None))}"
    )
    s2_stats = s2.get_stats()
    print("Transaction analysis:")
    for name, info in s2_stats.items():
        print(f"   - {name}: {info}")

    print("\nInitializing Event Stream...")
    s3 = EventStream("EVENT_001")
    d3 = ["login", "error", "logout"]
    print(
        f"Stream ID: {s3.id}, Type: {s3.type}\n"
        f"{s3.process_batch(s3.filter_data(d3, None))}"
    )
    s3_stats = s3.get_stats()
    print("Event analysis:")
    for name, info in s3_stats.items():
        print(f"   - {name}: {info}")

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")
    stream_manager = StreamProcessor()
    stream_manager.add_stream(s1)
    stream_manager.add_stream(s2)
    stream_manager.add_stream(s3)

    print("Batch 1 Stats:")
    filtered = 0
    for stream in stream_manager.streams:
        stats = stream.get_stats()
        print(
            f"   - {stream.id} data: "
            f"{stats.get("data processed")} data processed")
        filtered += stats.get("data filtered")
    print(
        "\nStream filtering active: High-priority data only\n"
        f"Filtered results: total of {filtered} data filtered"
    )
    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    stream_tester()