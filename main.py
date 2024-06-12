"""main module"""
import math

MIN_THRUST = 18
MAX_THRUST = 100
BOOST_DISTANCE_THRESHOLD = 6000
SAFE_DISTANCE = 800
AVOID_DISTANCE = 800

class Point:
    """Represents a point in 2D space."""

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def dist(self, other) -> int:
        """Calculate Euclidean distance to another point."""
        return round(math.hypot(self.x - other.x, self.y - other.y))

    def angle(self, other) -> float:
        """Calculate angle in radians to another point."""
        return math.atan2(other.y - self.y, other.x - self.x)

    def degree(self, other) -> float:
        """Calculate angle in degrees to another point."""
        return math.degrees(self.angle(other))


def compute_target(
        current: Point,
        next_cp: Point,
        distance: int,
        speed: Point,
        opponent: Point
    ) -> Point:
    """Determine the next target point for the pod, avoiding the opponent."""
    angle_rad = current.angle(next_cp)
    adjusted_distance = max(0, distance * 0.75 - speed.dist(Point(0, 0)) * 0.5)

    target = Point(
        round(current.x + math.cos(angle_rad) * adjusted_distance),
        round(current.y + math.sin(angle_rad) * adjusted_distance)
    )

    # Avoid opponent if too close
    if current.dist(opponent) < AVOID_DISTANCE:
        avoidance_angle = current.angle(opponent) + math.pi  # Opposite direction
        target = Point(
            round(current.x + math.cos(avoidance_angle) * AVOID_DISTANCE),
            round(current.y + math.sin(avoidance_angle) * AVOID_DISTANCE)
        )

    return target


def compute_thrust(distance: int, angle: int) -> int:
    """Calculate thrust based on the angle and distance to the next checkpoint."""
    if abs(angle) > 90:
        return MIN_THRUST
    elif distance < SAFE_DISTANCE:
        return round(MAX_THRUST * (distance / SAFE_DISTANCE))
    else:
        return round(MAX_THRUST * (1 - abs(angle) / 180))


def main():
    """Main function to control the pod."""
    boost_used = False
    previous = None  # Initialize the previous position as None

    while True:
        # Read input values
        current_x, current_y, next_checkpoint_x, next_checkpoint_y, \
            next_checkpoint_dist, next_checkpoint_angle = map(int, input().split())
        opponent_x, opponent_y = map(int, input().split())

        # Create point objects for the current position, next checkpoint, and opponent position
        current = Point(current_x, current_y)
        next_checkpoint = Point(next_checkpoint_x, next_checkpoint_y)
        opponent = Point(opponent_x, opponent_y)

        # Calculate the pod's current speed
        if previous is not None:
            speed = current - previous
        else:
            speed = Point(0, 0)
        previous = current

        # Calculate the target point and thrust, considering the opponent
        target = compute_target(current, next_checkpoint, next_checkpoint_dist, speed, opponent)
        thrust = compute_thrust(next_checkpoint_dist, next_checkpoint_angle)

        # Decide whether to use BOOST or not
        if not boost_used and next_checkpoint_dist >= BOOST_DISTANCE_THRESHOLD \
            and abs(next_checkpoint_angle) < 10:
            print(target.x, target.y, "BOOST")
            boost_used = True
        else:
            print(target.x, target.y, thrust)


if __name__ == "__main__":
    main()
