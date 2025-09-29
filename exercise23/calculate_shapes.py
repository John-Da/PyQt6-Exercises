from shapes.circle import circle_area
from shapes.triangle import triangle_area
from shapes.rectangle import rectangle_area

from shapes.three_d_shpaes.cube import cube_volume
from shapes.three_d_shpaes.sphere import sphere_volume
from shapes.three_d_shpaes.cylinder import cylinder_volume


print("2D Shapes:")
print(f"Circle area ( radius 5 ): {circle_area(5):.2f}")
print(f"Rectangle area (4x6): {rectangle_area(4, 6):.2f}")
print(f"Triangle area (base 3, height 8): {triangle_area(3, 8):.2f}")

print("\n3D Shapes:")
print(f"Cube volume (side 3): {cube_volume(3):.2f}")
print(f"Sphere volume (radius 4): {sphere_volume(4):.2f}")
print(f"Cylinder volume (radius 2, height 5): {cylinder_volume(2, 5):.2f}")
