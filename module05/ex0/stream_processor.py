from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if not isinstance(data, list):
            return False
        for n in data:
            if not isinstance(n, (int, float)):
                return False
        return True

    def process(self, data: Any) -> str:
        print(f"Processing data: {data}")
        if not self.validate(data):
            print("Validation: Numeric data verification failed")
            return "ERROR detected: Numeric data verification error"
        print("Validation: Text data verified")
        size = len(data)
        total = sum(data)
        if (size > 0):
            avg = total / size
        else:
            avg = 0.0
        return f"Processed {size} numeric values, sum={total}, avg={avg}"

    def format_output(self, result: str) -> str:
        if "ERROR" in result:
            return f"Output: [ALERT] {result}"
        return super().format_output(result)


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        return True

    def process(self, data: Any) -> str:
        print(f"Processing data: {data}")
        if not self.validate(data):
            print("Validation: Text data verification failed")
            return "ERROR detected: Text data verification failed"
        print("Validation: Text data verified")
        length = len(data)
        words = len(data.split())
        return f"Processed text: {length} characters, {words} words"

    def format_output(self, result: str) -> str:
        if "ERROR" in result:
            return f"Output: [ALERT] {result}"
        return super().format_output(result)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        if "ERROR" in data or "INFO" in data:
            return True
        return False

    def process(self, data: Any) -> str:
        print(f"Processing data: {data}")
        if not self.validate(data):
            print("Validation: Log entry verification failed")
            return "ERROR detected: Log entry verification failed"
        print("Validation: Log entry verified")
        log_data = data.split(':', 1)
        if log_data[0] == "ERROR":
            return f"ERROR level detected:{log_data[1]}"
        else:
            return f"Processed log entry:{log_data[1]}"

    def format_output(self, result: str) -> str:
        if "ERROR" in result:
            return f"Output: [ALERT] {result}"
        return super().format_output(result)


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    num_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()

    # Numeric Processor
    num_list1 = [1, 2, 3, 4, 5]
    num_list2 = ["bad", 2, 3, 4, 5]
    print("Initializing Numeric Processor (GOOD)...")
    res1 = num_proc.process(num_list1)
    print(num_proc.format_output(res1))
    print("\nInitializing Numeric Processor (BAD)...")
    res2 = num_proc.process(num_list2)
    print(num_proc.format_output(res2))

    # Text Processor
    text1 = "Hello Nexus World"
    print("\nInitializing Text Processor (GOOD)...")
    res3 = text_proc.process(text1)
    print(text_proc.format_output(res3))
    print("\nInitializing Text Processor (BAD)...")
    res4 = text_proc.process(num_list1)
    print(text_proc.format_output(res4))

    # Log Processor
    log1 = "ERROR: Connection timeout"
    log2 = "INFO: Logged in"
    print("\nInitializing Log Processor (GOOD1)...")
    res5 = log_proc.process(log1)
    print(log_proc.format_output(res5))
    print("\nInitializing Log Processor (GOOD2)...")
    res6 = log_proc.process(log2)
    print(log_proc.format_output(res6))
    print("\nInitializing Log Processor (BAD)...")
    res7 = log_proc.process(text1)
    print(log_proc.format_output(res7))

    # Polymorphic
    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...\n")
    nexus_stream: List[DataProcessor] = [
        num_proc, text_proc, log_proc
    ]
    inputs: List[Any] = [
        [1, 2, 3], "Hello Nexus", "INFO: System ready"
    ]
    for i, (proc, data) in enumerate(zip(nexus_stream, inputs), 1):
        result = proc.format_output(proc.process(data))
        print(f"Result {i}: {result}\n")
    print("\nFoundation systems online. NExus ready for advanced streams.")


if __name__ == "__main__":
    main()