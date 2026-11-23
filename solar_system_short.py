import pyvista as pv
import numpy as np

# 1. YouTube Shorts ke liye Vertical 9:16 Resolution (1080x1920)
plotter = pv.Plotter(off_screen=True, window_size=(1080, 1920))
plotter.set_background("#02010a")

# 2. Peeche Deep Space Stars add karna
np.random.seed(2026)
stars = np.random.uniform(-35, 35, size=(900, 3))
plotter.add_mesh(pv.PolyData(stars), color="white", point_size=3, render_points_as_spheres=True)

# 3. Center mein Glowing Sun (Sooraj)
sun = pv.Sphere(radius=1.8, theta_resolution=60, phi_resolution=60)
plotter.add_mesh(sun, color="#ffb703", smooth_shading=True, specular=1.0)
# Sun ke gird halka glowing corona aura
sun_glow = pv.Sphere(radius=2.1, theta_resolution=40, phi_resolution=40)
plotter.add_mesh(sun_glow, color="#fb8500", opacity=0.25, smooth_shading=True)

# 4. Planets Data: (Name, Orbit_Radius, Planet_Size, Speed, Color, Start_Angle)
planets_data = [
    ("Mercury", 2.8, 0.22, 0.085, "#adb5bd", 0.5),
    ("Venus",   3.8, 0.34, 0.065, "#e9c46a", 2.1),
    ("Earth",   5.0, 0.38, 0.050, "#00bbf9", 4.0),
    ("Mars",    6.2, 0.30, 0.040, "#e76f51", 1.2),
    ("Jupiter", 8.2, 0.85, 0.025, "#f4a261", 3.3),
    ("Saturn",  10.6, 0.72, 0.019, "#fee440", 5.2),
    ("Uranus",  12.8, 0.50, 0.014, "#00f5d4", 0.9),
    ("Neptune", 14.8, 0.48, 0.011, "#3a86ff", 2.8),
]

planet_actors = []
saturn_ring_actor = None

# Har Planet aur uska Glowing 3D Orbit Ring banana
for name, dist, size, speed, color, start_ang in planets_data:
    # Orbit Circle Path
    theta = np.linspace(0, 2 * np.pi, 200)
    orbit_pts = np.column_stack((dist * np.cos(theta), dist * np.sin(theta), np.zeros_like(theta)))
    orbit_line = pv.Spline(orbit_pts, 200).tube(radius=0.025)
    plotter.add_mesh(orbit_line, color=color, opacity=0.35)
    
    # Planet Sphere (Initial position (0,0,0) par banayenge aur frame loop mein move karenge)
    p_mesh = pv.Sphere(radius=size, theta_resolution=45, phi_resolution=45)
    actor = plotter.add_mesh(p_mesh, color=color, smooth_shading=True, specular=0.6)
    
    # Agar Saturn hai toh uske gird Rings bhi add karna
    if name == "Saturn":
        ring = pv.Disc(center=(0, 0, 0), inner=size * 1.35, outer=size * 2.2, r_res=5, c_res=80)
        ring.rotate_x(25, inplace=True)
        saturn_ring_actor = plotter.add_mesh(ring, color="#e9c46a", opacity=0.8, smooth_shading=True)
        
    planet_actors.append({
        "name": name,
        "dist": dist,
        "speed": speed,
        "angle": start_ang,
        "actor": actor
    })

# 5. Top Hook Text & Channel Branding
plotter.add_text("3D Solar System Orbits\nin Pure Python", position="upper_edge", color="white", font_size=18)
plotter.add_text("@CyberCode3D", position="lower_edge", color="#00f5d4", font_size=13)

# Camera ko cinematic top-angled view par set karna
plotter.camera_position = [(0, -24, 14), (0, 0, 0), (0, 0, 1)]

# 6. 15 Seconds ki Smooth MP4 Video Export (30 FPS x 15 sec = 450 frames)
output_file = "solar_system_short.mp4"
plotter.open_movie(output_file, framerate=30, quality=8)

print("Rendering 3D Solar System Orbits (450 Frames)...")

for frame in range(450):
    # Har planet ko uske orbit mein aage badhana
    for p in planet_actors:
        current_angle = p["angle"] + frame * p["speed"]
        px = p["dist"] * np.cos(current_angle)
        py = p["dist"] * np.sin(current_angle)
        p["actor"].SetPosition(px, py, 0)
        
        # Saturn ke rings ko Saturn ke sath move karna
        if p["name"] == "Saturn" and saturn_ring_actor is not None:
            saturn_ring_actor.SetPosition(px, py, 0)
            
    # Camera ko halka sa cinematic orbit mein ghumana
    plotter.camera.azimuth += 0.45
    plotter.camera.elevation = 28 + 8 * np.sin(frame * 0.02)
    
    plotter.write_frame()

plotter.close()
print("Ready! Aapki YouTube Short 'solar_system_short.mp4' save ho gayi hai!")
