import bpy
import math
import os

print("=== START BLENDER SCRIPT PADUKA SAMBAS ===")

# Buat folder output
cwd = os.getcwd()
out_dir = os.path.join(cwd, "output")
os.makedirs(out_dir, exist_ok=True)
out_file = os.path.join(out_dir, "paduka_sambas.png")

print(f"Target Output Path: {out_file}")

# Bersihkan dan buat scene
bpy.ops.wm.read_factory_settings(use_empty=True)

# Tambahkan Text
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

# Set render ke format image langsung
scene = bpy.context.scene
scene.render.resolution_x = 1280
scene.render.resolution_y = 720
scene.render.filepath = out_file

# Render frame
print("Memanggil bpy.ops.render.render...")
bpy.ops.render.render(write_still=True)

if os.path.exists(out_file):
    print(f"BERHASIL: File ditemukan sebesar {os.path.getsize(out_file)} bytes")
else:
    print("WARNING: File belum ada, mencoba menyimpan manual...")
    # Alternatif simpan gambar hasil render
    img = bpy.data.images.get('Render Result')
    if img:
        img.save_render(out_file)
        print(f"Saved via save_render: {os.path.exists(out_file)}")

print("=== FINISH BLENDER SCRIPT ===")
