from pydantic import BaseModel
from typing import List, Optional

class Route(BaseModel):
    route_no: int
    travel_date: str  # Format: YYYY-MM-DD
    origin: str
    transport_modes: str  # Example: "Bus → Flight"
    stops: str  # Example: "Atru (07:00) → Jaipur (11:45) → Pune"
    operators: str  # Example: "RSRTC, IndiGo"
    departure_arrival: str  # Example: "07:00 - 16:35"
    total_time: str  # Example: "9h 35m"
    total_cost: str  # Example: "Rs.9500"

class Traveler(BaseModel):
    name: str
    routes: List[Route]

class RouteIdentifierOutput(BaseModel):
    travelers: List[Traveler]
