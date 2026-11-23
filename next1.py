import pyvista as pv

plotter = pv.Plotter(off_screen=True, window_size=(1080, 1080))
plotter.set_background("#03050f")

# Nested 3D Hexagonal Rings (Layers mein)
layers = [
    (2.8, 0.25, "#f72585", 0),
    (2.1, 0.35, "#00bbf9", 15),
    (1.4, 0.45, "#00f5d4", 30),
]

for rad, height, col, rot in layers:
    hex_ring = pv.Cylinder(center=(0, 0, 0), direction=(0, 0, 1), radius=rad, height=height, resolution=6)
    hex_ring.rotate_z(rot, inplace=True)
    plotter.add_mesh(hex_ring, color=col, smooth_shading=False, metallic=0.7, specular=0.9)
    plotter.add_mesh(hex_ring, style="wireframe", color="white", line_width=2)

# Top-down 3D isometric angle set karna
plotter.camera_position = [(0, -4.5, 6.5), (0, 0, 0), (0, 1, 0)]
plotter.show(screenshot="pro_logo_hex.png")
print("Saved: pro_logo_hex.png")
