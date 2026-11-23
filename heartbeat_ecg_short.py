import pyvista as pv
import numpy as np

# 1. YouTube Shorts ke liye Vertical 9:16 Resolution (1080x1920)
plotter = pv.Plotter(off_screen=True, window_size=(1080, 1920))
plotter.set_background("#02050e")

# 2. Hologram Floor Grid (Medical Sci-Fi Base)
grid_plane = pv.Plane(center=(0, 0, -1.8), direction=(0, 0, 1), i_size=18, j_size=8, i_resolution=36, j_resolution=16)
plotter.add_mesh(grid_plane, style="wireframe", color="#00bbf9", opacity=0.18, line_width=1.2)

# Peeche tairte hue cyber-hologram particles
np.random.seed(2026)
stars = np.random.uniform(-9, 9, size=(350, 3))
plotter.add_mesh(pv.PolyData(stars), color="#00f5d4", point_size=3, render_points_as_spheres=True, opacity=0.6)

# 3. Asli Heartbeat (P-QRS-T ECG Wave) Mathematical Function
def ecg_waveform(x_vals):
    # Har 5.0 units ke baad ek heartbeat cycle repeat hogi
    phase = np.mod(x_vals, 5.0)
    
    # P-wave (halka upar)
    p_wave = 0.25 * np.exp(-((phase - 1.2) ** 2) / 0.06)
    # Q-dip (thoda neeche)
    q_wave = -0.30 * np.exp(-((phase - 1.95) ** 2) / 0.01)
    # R-spike (tez aur lamba main heartbeat spike!)
    r_wave = 2.60 * np.exp(-((phase - 2.15) ** 2) / 0.015)
    # S-dip (neeche jhatka)
    s_wave = -0.65 * np.exp(-((phase - 2.35) ** 2) / 0.012)
    # T-wave (recovery bump)
    t_wave = 0.45 * np.exp(-((phase - 3.3) ** 2) / 0.12)
    
    return p_wave + q_wave + r_wave + s_wave + t_wave

# 4. Initial ECG Wave Tube & Glowing Laser Tip setup
num_pts = 350
x_window = np.linspace(-7.0, 5.0, num_pts)
y_zeros = np.zeros(num_pts)
z_init = ecg_waveform(x_window)

ecg_points = np.column_stack((x_window, y_zeros, z_init))
ecg_spline = pv.Spline(ecg_points, num_pts)
ecg_tube = ecg_spline.tube(radius=0.09)
ecg_tube["PulseGlow"] = np.linspace(0, 1, ecg_tube.n_points)

wave_actor = plotter.add_mesh(
    ecg_tube,
    scalars="PulseGlow",
    cmap="cool",  # Dark Blue tail -> Bright Cyan/Pink leading edge
    smooth_shading=True,
    specular=0.95,
    show_scalar_bar=False
)

# Leading Tip par ek chamakta hua Glowing Sphere (Heartbeat Pulse Head)
tip_sphere = pv.Sphere(radius=0.24, center=(0, 0, 0))
tip_actor = plotter.add_mesh(tip_sphere, color="#ff007f", smooth_shading=True, specular=1.0)
tip_actor.SetPosition(x_window[-1], 0, z_init[-1])

# 5. Top Hook Text & Channel Branding
plotter.add_text("3D Heartbeat ECG Wave\nin Pure Python", position="upper_edge", color="white", font_size=18)
plotter.add_text("@CyberCode3D", position="lower_edge", color="#00f5d4", font_size=13)

# Cinematic 3D side-angled camera
plotter.camera_position = [(1.5, -13.5, 4.5), (-0.5, 0, 0.2), (0, 0, 1)]

# 6. 15 Seconds ki Smooth ECG Animation Export (30 FPS x 15 sec = 450 frames)
output_file = "heartbeat_ecg_short.mp4"
plotter.open_movie(output_file, framerate=30, quality=8)

print("Rendering 3D Heartbeat ECG Hologram (450 Frames)...")

for frame in range(450):
    shift = frame * 0.085  # Wave ki aage badhne ki speed
    current_x = x_window + shift
    current_z = ecg_waveform(current_x)
    
    # Screen par wave ko fixed window [-7, 5] mein dikhana taake chalti hui lage
    display_pts = np.column_stack((x_window, y_zeros, current_z))
    new_spline = pv.Spline(display_pts, num_pts)
    new_tube = new_spline.tube(radius=0.09)
    new_tube["PulseGlow"] = np.linspace(0, 1, new_tube.n_points)
    
    # Mesh aur glowing tip ko update karna
    wave_actor.mapper.SetInputData(new_tube)
    tip_actor.SetPosition(x_window[-1], 0, current_z[-1])
    
    # Camera ko halka sa breathing motion dena
    plotter.camera.azimuth = 8 * np.sin(frame * 0.02)
    plotter.write_frame()

plotter.close()
print("Ready! Aapki YouTube Short 'heartbeat_ecg_short.mp4' save ho gayi hai!")
