from enum import Enum
from datetime import datetime
from typing import List
from pydantic import BaseModel, Field, model_validator, ValidationError


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def check_safety_requirements(self) -> 'SpaceMission':
        if not self.mission_id[0] == 'M':
            raise ValueError("Mission ID must start with 'M'.")

        count = 0
        for c in self.crew:
            if not c.is_active:
                raise ValueError("All crew members must be active.")
            if c.rank in (Rank.CAPTAIN, Rank.COMMANDER):
                count += 1
        if count < 1:
            raise ValueError("Must have at least one Commander or Captain.")

        if self.duration_days > 365:
            count = 0
            for c in self.crew:
                if c.years_experience >= 5:
                    count += 1
            if count / len(self.crew) < 0.5:
                raise ValueError(
                    "Long missions (>365 days) need 50%"
                    " experienced crew(5+ years)."
                )
        return self

    def print_info(self) -> None:
        print(f"Mission: {self.mission_name}")
        print(f"ID: {self.mission_id}")
        print(f"Destination: {self.destination}")
        print(f"Duration: {self.duration_days} days")
        print(f"Budget: {self.budget_millions}M")
        print(f"Crew size: {len(self.crew)}")
        print("Crew members:")
        for c in self.crew:
            print(f"- {c.name} ({c.rank.value}) - {c.specialization}")


def main() -> None:
    print("\nSpace Mission Crew Validation")
    print("========================================")

    sarah = CrewMember(
        member_id="mem1",
        name="Sarah Connor",
        rank=Rank.COMMANDER,
        age=21,
        specialization="Mission Command",
        years_experience=6
    )
    john = CrewMember(
        member_id="mem2",
        name="John Smith",
        rank=Rank.LIEUTENANT,
        age=21,
        specialization="Navigation",
        years_experience=6
    )
    alice = CrewMember(
        member_id="mem3",
        name="Alice Johnson",
        rank=Rank.OFFICER,
        age=21,
        specialization="Engineering",
        years_experience=6
    )
    crews = [sarah, john, alice]
    sm1 = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime.now(),
        duration_days=900,
        crew=crews,
        budget_millions=2500.0
    )

    print("Valid mission created:")
    sm1.print_info()

    print("\n========================================")
    print("Expected validation error:")

    bokim = CrewMember(
        member_id="mem4",
        name="Sarah Connor",
        rank=Rank.CADET,
        age=21,
        specialization="Fool around",
        years_experience=6
    )
    new_crew = [bokim, john, alice]
    try:
        sm1 = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=new_crew,
            budget_millions=2500.0
        )
    except ValidationError as e:
        for error in e.errors():
            print(error['msg'].replace("Value error, ", ""))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
