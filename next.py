import pyvista as pv

plotter = pv.Plotter(off_screen=True, window_size=(1080, 1080))
plotter.set_background("#04020d")

# 1. Center Glowing Energy Core (Icosahedron Crystal)
core = pv.Icosahedron(radius=1.15)
plotter.add_mesh(core, color="#00f5d4", smooth_shading=True, metallic=0.8, specular=1.0)
plotter.add_mesh(core, style="wireframe", color="white", line_width=2.5)

# 2. 3 Intersecting Gyroscope Neon Rings
angles = [(65, 20, "#f72585"), (-65, 20, "#00bbf9"), (0, 85, "#fee440")]
for rx, ry, col in angles:
    ring = pv.ParametricTorus(ringradius=2.5, crosssectionradius=0.11)
    ring.rotate_x(rx, inplace=True)
    ring.rotate_y(ry, inplace=True)
    plotter.add_mesh(ring, color=col, smooth_shading=True, metallic=0.6, specular=0.9)

plotter.show(screenshot="pro_logo_atom.png")
print("Saved: pro_logo_atom.png")
