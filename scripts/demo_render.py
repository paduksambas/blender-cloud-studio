import bpy
import math
import sys
import os

print("=== Menjalankan Script Blender 3D Paduka Sambas ===")

# Buat direktori output
output_dir = os.path.join(os.getcwd(), "output")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "paduka_sambas_render.png")

# Reset scene
bpy.ops.wm.read_factory_settings(use_empty=True)

# Tambahkan Teks 3D
bpy.ops.object.text_add(location=(0, 0, 0))
txt = bpy.context.active_object
txt.data.body = "PADUKA SAMBAS"
txt.data.align_x = 'CENTER'
txt.data.align_y = 'MIDDLE'
txt.data.extrude = 0.15
txt.rotation_euler = (math.radians(90), 0, 0)

# Tambahkan Light
bpy.ops.object.light_add(type='SUN', location=(5, -5, 10))
sun = bpy.context.active_object
sun.data.energy = 5.0

# Tambahkan Kamera
bpy.ops.object.camera_add(location=(0, -8, 0.5))
cam = bpy.context.active_object
cam.rotation_euler = (math.radians(90), 0, 0)
bpy.context.scene.camera = cam

# Set render settings (Gunakan EEVEE / BLENDER_EEVEE_NEXT atau CYCLES CPU sederhana)
scene = bpy.context.scene
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
scene.render.image_settings.file_format = 'PNG'
scene.render.filepath = output_path

print(f"Render dimulai ke: {output_path}")
bpy.ops.render.render(write_still=True)
print("Render Selesai 100%!")
