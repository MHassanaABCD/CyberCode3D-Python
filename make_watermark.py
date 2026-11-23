import pyvista as pv

# Exact 150x150 pixels size jo YouTube Video Watermark mein chahiye
plotter = pv.Plotter(off_screen=True, window_size=(150, 150))
plotter.set_background("#050214")

# Center Crystal Core
core = pv.Icosahedron(radius=1.1)
plotter.add_mesh(core, color="#00f5d4", smooth_shading=True, specular=1.0)

# Glowing Neon Rings
angles = [(65, 20, "#f72585"), (-65, 20, "#00bbf9"), (0, 85, "#fee440")]
for rx, ry, col in angles:
    ring = pv.ParametricTorus(ringradius=2.4, crosssectionradius=0.18)
    ring.rotate_x(rx, inplace=True)
    ring.rotate_y(ry, inplace=True)
    plotter.add_mesh(ring, color=col, smooth_shading=True)

plotter.show(screenshot="watermark_150.png")
print("Ready! Ab 'watermark_150.png' ko YouTube ke Video Watermark mein Upload karein.")
