import bpy
import math
import sys
import os

# Ambil argumen resolusi jika ada
argv = sys.argv
if "--" in argv:
    args = argv[argv.index("--") + 1:]
    res_x = int(args[0]) if len(args) > 0 else 1920
    res_y = int(args[1]) if len(args) > 1 else 1080
else:
    res_x, res_y = 1920, 1080

print(f"=== Menjalankan Script Blender 3D Paduka Sambas (Resolusi: {res_x}x{res_y}) ===")

# 1. Bersihkan scene default
bpy.ops.wm.read_factory_settings(use_empty=True)

# 2. Buat World & Background
world = bpy.data.worlds.new("StudioWorld")
bpy.context.scene.world = world
world.use_nodes = True
bg_node = world.node_tree.nodes.get("Background")
if bg_node:
    bg_node.inputs[0].default_value = (0.02, 0.03, 0.05, 1.0) # Dark Navy Elegant
    bg_node.inputs[1].default_value = 1.0

# 3. Buat Teks 3D "PADUKA SAMBAS"
bpy.ops.object.text_add(location=(0, 0, 0))
text_obj = bpy.context.active_object
text_obj.name = "TitleText"
text_obj.data.body = "PADUKA SAMBAS"
text_obj.data.align_x = 'CENTER'
text_obj.data.align_y = 'MIDDLE'
text_obj.data.extrude = 0.12
text_obj.data.bevel_depth = 0.02
text_obj.data.bevel_resolution = 4
text_obj.rotation_euler = (math.radians(90), 0, 0)

# Buat Subtext "BLENDER CLOUD STUDIO"
bpy.ops.object.text_add(location=(0, -0.2, -0.6))
subtext_obj = bpy.context.active_object
subtext_obj.name = "SubText"
subtext_obj.data.body = "BLENDER CLOUD RUNNER"
subtext_obj.data.align_x = 'CENTER'
subtext_obj.data.align_y = 'MIDDLE'
subtext_obj.data.extrude = 0.05
subtext_obj.data.bevel_depth = 0.01
subtext_obj.data.size = 0.4
subtext_obj.rotation_euler = (math.radians(90), 0, 0)

# 4. Tambahkan Material Emas Mewah (Gold Metallic)
mat_gold = bpy.data.materials.new(name="GoldMaterial")
mat_gold.use_nodes = True
bsdf_gold = mat_gold.node_tree.nodes.get("Principled BSDF")
if bsdf_gold:
    # Warna Emas/Kuning Mewah
    bsdf_gold.inputs['Base Color'].default_value = (1.0, 0.766, 0.336, 1.0)
    bsdf_gold.inputs['Metallic'].default_value = 0.95
    bsdf_gold.inputs['Roughness'].default_value = 0.18
text_obj.data.materials.append(mat_gold)

# Material Emerald / Cyan untuk Subtext
mat_cyan = bpy.data.materials.new(name="CyanMaterial")
mat_cyan.use_nodes = True
bsdf_cyan = mat_cyan.node_tree.nodes.get("Principled BSDF")
if bsdf_cyan:
    bsdf_cyan.inputs['Base Color'].default_value = (0.05, 0.8, 0.6, 1.0)
    bsdf_cyan.inputs['Metallic'].default_value = 0.8
    bsdf_cyan.inputs['Roughness'].default_value = 0.25
subtext_obj.data.materials.append(mat_cyan)

# 5. Tambahkan Lantai Reflektif (Plane)
bpy.ops.mesh.primitive_plane_add(size=30, location=(0, 0, -1.0))
floor = bpy.context.active_object
mat_floor = bpy.data.materials.new(name="FloorMaterial")
mat_floor.use_nodes = True
bsdf_floor = mat_floor.node_tree.nodes.get("Principled BSDF")
if bsdf_floor:
    bsdf_floor.inputs['Base Color'].default_value = (0.015, 0.02, 0.03, 1.0)
    bsdf_floor.inputs['Metallic'].default_value = 0.5
    bsdf_floor.inputs['Roughness'].default_value = 0.15
floor.data.materials.append(mat_floor)

# 6. Pencahayaan Studio (Three-Point Lighting)
# Key Light (Warm Sun)
bpy.ops.object.light_add(type='POINT', location=(4, -6, 5))
key_light = bpy.context.active_object
key_light.data.energy = 2500
key_light.data.color = (1.0, 0.95, 0.85)

# Fill Light (Cool Teal)
bpy.ops.object.light_add(type='POINT', location=(-5, -5, 3))
fill_light = bpy.context.active_object
fill_light.data.energy = 1500
fill_light.data.color = (0.4, 0.8, 1.0)

# Rim/Back Light
bpy.ops.object.light_add(type='POINT', location=(0, 4, 3))
rim_light = bpy.context.active_object
rim_light.data.energy = 2000
rim_light.data.color = (1.0, 0.6, 0.2)

# 7. Kamera
bpy.ops.object.camera_add(location=(0, -7.5, 0.8))
camera = bpy.context.active_object
camera.rotation_euler = (math.radians(84), 0, 0)
bpy.context.scene.camera = camera

# 8. Konfigurasi Render Engine
scene = bpy.context.scene
scene.render.engine = 'CYCLES'
scene.cycles.device = 'CPU'
scene.cycles.samples = 64  # Cepat tapi bersih untuk cloud runner
scene.render.resolution_x = res_x
scene.render.resolution_y = res_y
scene.render.resolution_percentage = 100

# Pastikan folder output ada
output_dir = os.path.abspath("output")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "paduka_sambas_render.png")
scene.render.filepath = output_path

print(f"Memulai rendering ke: {output_path} ...")
bpy.ops.render.render(write_still=True)
print("Rendering selesai 100%!")
