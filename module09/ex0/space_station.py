from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=50)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(None, max_length=200)

    def print_info(self) -> None:
        print(f"ID: {self.station_id}")
        print(f"Name: {self.name}")
        print(f"Crew: {self.crew_size} people")
        print(f"Power: {self.power_level}%")
        print(f"Oxygen: {self.oxygen_level}%")
        print(
            "Status: Operational"
            if self.is_operational
            else "Status: Not operational"
        )


def main() -> None:
    print("\nSpace Station Data Validation")
    print("========================================")
    ss1 = SpaceStation(
        station_id="ISS001",
        name="Interational Space Station",
        crew_size=6, power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime.now(),
        is_operational=True
    )

    print("Valide station created:")
    ss1.print_info()

    print("\n========================================")
    print("Expected validation error:")

    try:
        SpaceStation(
            station_id="ISS001",
            name="Interational Space Station",
            crew_size=21,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
            is_operational=True
        )
    except ValidationError as e:
        for error in e.errors():
            print(f"{error['msg']}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
