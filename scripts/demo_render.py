import bpy
import math
import os

print("=== START BLENDER SCRIPT PADUKA SAMBAS ===")

# Reset factory
bpy.ops.wm.read_factory_settings(use_empty=True)

# Tambahkan Text 3D
bpy.ops.object.text_add(location=(0, 0, 0))
txt = bpy.context.active_object
txt.data.body = "PADUKA SAMBAS"
txt.data.align_x = 'CENTER'
txt.data.align_y = 'MIDDLE'
txt.data.extrude = 0.2
txt.rotation_euler = (math.radians(90), 0, 0)

# Tambahkan Light
bpy.ops.object.light_add(type='SUN', location=(5, -5, 10))

# Tambahkan Camera
bpy.ops.object.camera_add(location=(0, -6, 0.5))
cam = bpy.context.active_object
cam.rotation_euler = (math.radians(90), 0, 0)
bpy.context.scene.camera = cam

# Set Cycles CPU agar bisa render headless tanpa GPU window
scene = bpy.context.scene
scene.render.engine = 'CYCLES'
scene.cycles.device = 'CPU'
scene.cycles.samples = 16

# Simpan scene ke file .blend
blend_out = os.path.join(os.getcwd(), "blend_files", "paduka_sambas.blend")
os.makedirs(os.path.dirname(blend_out), exist_ok=True)
bpy.ops.wm.save_as_mainfile(filepath=blend_out)
print(f"File blend berhasil dibuat: {blend_out}")

print("=== FINISH BLENDER SCRIPT ===")
