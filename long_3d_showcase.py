import pyvista as pv
import numpy as np

# Full HD 16:9 Landscape Resolution (Long Video Format)
plotter = pv.Plotter(off_screen=True, window_size=(1920, 1080))
plotter.set_background("#04020e")

# 45 Seconds Video @ 30 FPS = 1350 Total Frames (Har scene ~11 seconds)
output_file = "cybercode3d_showcase.mp4"
plotter.open_movie(output_file, framerate=30, quality=8)

print("Video render shuru ho rahi hai (45 Seconds / 1350 Frames)...")
print("Is mein 2 se 4 minute lag sakte hain, terminal band na karein...")

plotter.clear()
plotter.set_background("#04020e")

core = pv.Icosahedron(radius=1.2)
plotter.add_mesh(core, color="#00f5d4", smooth_shading=True, metallic=0.8, specular=1.0)
plotter.add_mesh(core, style="wireframe", color="white", line_width=2)

ring_specs = [(65, 20, "#f72585"), (-65, 20, "#00bbf9"), (0, 85, "#fee440")]
for rx, ry, col in ring_specs:
    ring = pv.ParametricTorus(ringradius=2.6, crosssectionradius=0.11)
    ring.rotate_x(rx, inplace=True)
    ring.rotate_y(ry, inplace=True)
    plotter.add_mesh(ring, color=col, smooth_shading=True, metallic=0.6, specular=0.9)

np.random.seed(10)
stars = np.random.uniform(-10, 10, size=(500, 3))
plotter.add_mesh(pv.PolyData(stars), color="white", point_size=3, render_points_as_spheres=True)

plotter.add_text("CyberCode3D // 01. QUANTUM ATOM CORE", position="upper_left", color="#00f5d4", font_size=16)
plotter.camera_position = [(0, -9, 3), (0, 0, 0), (0, 0, 1)]

for f in range(338):
    plotter.camera.azimuth += 1.06
    plotter.camera.elevation = 20 * np.sin(f * 0.02)
    plotter.write_frame()
print("Scene 1 Complete (25%)")


plotter.set_background("#050414")

t = np.linspace(0, 6 * np.pi, 300)
s1_pts = np.column_stack((2.0 * np.cos(t), 2.0 * np.sin(t), 0.55 * t - 5.0))
s2_pts = np.column_stack((2.0 * np.cos(t + np.pi), 2.0 * np.sin(t + np.pi), 0.55 * t - 5.0))

plotter.add_mesh(pv.Spline(s1_pts, 300).tube(radius=0.14), color="#00f5d4", smooth_shading=True, specular=0.8)
plotter.add_mesh(pv.Spline(s2_pts, 300).tube(radius=0.14), color="#f72585", smooth_shading=True, specular=0.8)

rung_colors = ["#fee440", "#00bbf9", "#9b5de5", "#00f5d4"]
for i in range(0, len(t), 10):
    rung = pv.Line(s1_pts[i], s2_pts[i]).tube(radius=0.06)
    plotter.add_mesh(rung, color=rung_colors[(i // 10) % 4], smooth_shading=True)
    plotter.add_mesh(pv.Sphere(radius=0.22, center=s1_pts[i]), color="#00f5d4", smooth_shading=True)
    plotter.add_mesh(pv.Sphere(radius=0.22, center=s2_pts[i]), color="#f72585", smooth_shading=True)

plotter.add_text("CyberCode3D // 02. GENETIC DNA HELIX", position="upper_left", color="#f72585", font_size=16)
plotter.camera_position = [(0, -14, 0), (0, 0, 0), (0, 0, 1)]

for f in range(337):
    plotter.camera.azimuth += 1.07
    plotter.camera.elevation = 25 * np.cos(f * 0.02)
    plotter.write_frame()
print("Scene 2 Complete (50%)")


plotter.clear()
plotter.set_background("#03010a")

gx = np.linspace(-10, 10, 150)
gy = np.linspace(-10, 10, 150)
GX, GY = np.meshgrid(gx, gy)
R = np.sqrt(GX**2 + GY**2)
TH = np.arctan2(GY, GX)
GZ = 2.2 * np.sin(R * 1.3 - 2 * TH) * np.exp(-0.12 * R)

wave_grid = pv.StructuredGrid(GX, GY, GZ)
wave_grid["Energy"] = (GZ + 0.3 * np.cos(3 * TH)).ravel(order="F")

plotter.add_mesh(wave_grid, scalars="Energy", cmap="plasma", smooth_shading=True, specular=0.7, show_scalar_bar=False)
plotter.add_text("CyberCode3D // 03. COSMIC ENERGY WAVE", position="upper_left", color="#fee440", font_size=16)
plotter.camera_position = [(0, -22, 12), (0, 0, 0), (0, 0, 1)]

for f in range(337):
    plotter.camera.azimuth += 1.07
    plotter.camera.elevation = 25 + 12 * np.sin(f * 0.02)
    plotter.write_frame()
print("Scene 3 Complete (75%)")


plotter.clear()
plotter.set_background("#02010a")

wz = np.linspace(0, 80.0, 280)
wtheta = np.linspace(0, 2 * np.pi, 55)
WZ, WTH = np.meshgrid(wz, wtheta)
cx = 2.2 * np.sin(WZ * 0.14)
cy = 2.2 * np.cos(WZ * 0.11)
wrad = 3.2 + 0.35 * np.sin(WZ * 0.6 + 4 * WTH)

wormhole = pv.StructuredGrid(cx + wrad * np.cos(WTH), cy + wrad * np.sin(WTH), WZ)
wormhole["Neon"] = np.sin(WZ * 0.25 + 2 * WTH).ravel(order="F")

plotter.add_mesh(wormhole, scalars="Neon", cmap="cool", style="wireframe", line_width=2.0, show_scalar_bar=False)
plotter.add_mesh(wormhole, scalars="Neon", cmap="plasma", opacity=0.2, smooth_shading=True, show_scalar_bar=False)
plotter.add_text("CyberCode3D // 04. HYPERSPACE WORMHOLE", position="upper_left", color="#00bbf9", font_size=16)

z_steps = np.linspace(2.0, 58.0, 338)
for f, cam_z in enumerate(z_steps):
    cam_x = 2.2 * np.sin(cam_z * 0.14)
    cam_y = 2.2 * np.cos(cam_z * 0.11)
    look_z = cam_z + 6.0
    look_x = 2.2 * np.sin(look_z * 0.14)
    look_y = 2.2 * np.cos(look_z * 0.11)
    roll = f * 1.1
    
    plotter.camera.position = (cam_x, cam_y, cam_z)
    plotter.camera.focal_point = (look_x, look_y, look_z)
    plotter.camera.up = (np.sin(np.radians(roll)), np.cos(np.radians(roll)), 0)
    plotter.camera.view_angle = 75.0
    plotter.write_frame()

plotter.close()
print("Mubarak ho! Aapki 45-Second Full HD Video 'cybercode3d_showcase.mp4' ready hai!")
