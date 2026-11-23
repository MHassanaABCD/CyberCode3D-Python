import pyvista as pv

# 1080x1080 Square HD Logo Resolution
plotter = pv.Plotter(off_screen=True, window_size=(1080, 1080))
plotter.set_background("#050214")

# Outer Glowing Neon Ring
ring = pv.ParametricTorus(ringradius=2.6, crosssectionradius=0.14)
ring.rotate_x(35, inplace=True)
ring.rotate_y(-20, inplace=True)
plotter.add_mesh(ring, color="#f72585", smooth_shading=True, specular=0.9)

# Center 3D Glowing Crystal Cube
cube = pv.Cube(x_length=2.2, y_length=2.2, z_length=2.2)
cube.rotate_x(30, inplace=True)
cube.rotate_y(45, inplace=True)
plotter.add_mesh(cube, color="#00f5d4", opacity=0.85, smooth_shading=True, specular=0.9)
plotter.add_mesh(cube, style="wireframe", color="white", line_width=3)

# High-Res PNG Logo Save Karna
plotter.show(screenshot="channel_logo.png")
print("Done! Aapka 3D Profile Picture 'channel_logo.png' save ho gaya hai.")
