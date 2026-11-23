import pyvista as pv
import numpy as np

# 1. YouTube Shorts ke liye Vertical 9:16 Resolution (1080x1920)
plotter = pv.Plotter(off_screen=True, window_size=(1080, 1920))
plotter.set_background("#04010d")

# 2. High-Resolution Base Sphere points save karna
base_sphere = pv.Sphere(radius=2.0, theta_resolution=90, phi_resolution=90)
orig_points = base_sphere.points.copy()
x0, y0, z0 = orig_points[:, 0], orig_points[:, 1], orig_points[:, 2]

# Spherical angles calculate karna (morphing waves ke liye)
r0 = np.sqrt(x0**2 + y0**2 + z0**2)
theta = np.arctan2(y0, x0)
phi = np.arccos(np.clip(z0 / r0, -1.0, 1.0))

# Initial Sphere mesh add karna
sphere_mesh = base_sphere.copy()
sphere_mesh["PulseEnergy"] = np.zeros(sphere_mesh.n_points)

sphere_actor = plotter.add_mesh(
    sphere_mesh,
    scalars="PulseEnergy",
    cmap="plasma",  # Deep Purple -> Hot Pink -> Bright Yellow
    smooth_shading=True,
    metallic=0.65,
    specular=0.95,
    clim=[0.0, 1.0],
    show_scalar_bar=False
)

# 3. Bahar ek Glowing Neon Ring aur Space Particles add karna
outer_ring = pv.ParametricTorus(ringradius=3.5, crosssectionradius=0.06)
outer_ring.rotate_x(70, inplace=True)
plotter.add_mesh(outer_ring, color="#00f5d4", smooth_shading=True, specular=1.0)

np.random.seed(2026)
stars = np.random.uniform(-6.5, 6.5, size=(450, 3))
plotter.add_mesh(pv.PolyData(stars), color="#00bbf9", point_size=3.5, render_points_as_spheres=True)

# 4. Top Hook Text (CyberCode3D Branding ke sath)
plotter.add_text("3D Audio Energy Sphere\nin Pure Python", position="upper_edge", color="white", font_size=18)
plotter.add_text("@CyberCode3D", position="lower_edge", color="#00f5d4", font_size=13)

# 5. 15 Seconds ki Smooth Morphing MP4 Video Export (30 FPS x 15 sec = 450 frames)
output_file = "pulsing_sphere_short.mp4"
plotter.open_movie(output_file, framerate=30, quality=8)

print("Rendering 3D Pulsing Energy Sphere (450 Frames)...")

n_frames = 450
for frame in range(n_frames):
    t = frame * 0.12  # Animation speed
    
    # Beat-style rhythmic pulse (tez bass drop aur smooth recovery)
    beat = (np.sin(t * 1.5) ** 2) * 0.65
    
    # 3D Harmonic Waves (Spikes aur ripples banana)
    wave1 = np.sin(6 * theta + t * 2.0) * np.sin(5 * phi - t * 1.5)
    wave2 = 0.5 * np.cos(10 * theta - t * 3.0) * np.sin(8 * phi + t)
    
    displacement = 1.0 + beat * (0.65 * wave1 + 0.35 * wave2)
    
    # Naye 3D coordinates update karna
    new_points = np.column_stack((
        x0 * displacement,
        y0 * displacement,
        z0 * displacement
    ))
    
    sphere_mesh.points = new_points
    # Spikes ki unchai ke mutabiq glow color update karna
    energy_colors = np.clip((displacement - 0.65) / 0.85, 0.0, 1.0)
    sphere_mesh["PulseEnergy"] = energy_colors
    
    # Camera aur outer ring ko smoothly ghumana
    plotter.camera.azimuth += 1.4
    plotter.camera.elevation = 18 * np.sin(frame * 0.025)
    outer_ring.rotate_z(1.2, inplace=True)
    
    plotter.write_frame()

plotter.close()
print("Ready! Aapki YouTube Short 'pulsing_sphere_short.mp4' save ho gayi hai!")
