import bpy
import time

# Step 1: Create a cube
bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0))

# Step 2: Create a sphere
bpy.ops.mesh.primitive_uv_sphere_add(size=1, location=(1, 0, 0))

# Step 3: Parent the sphere to the cube
bpy.context.object.parent = bpy.context.object
bpy.context.object.location = (0, 0, 0)

# Step 4: Keyframes
for frame in range(1, 101):
    # Move the cube
    bpy.context.object.location = (frame * 1, 0, 0)
    
    # Set the current frame
    bpy.context.scene.frame_set(frame)
    # Update the scene to see the changes
    bpy.context.view_layer.update()
    
    # Add a delay to slow down the animation
    time.sleep(0.01)

# Step 5: Render the animation
bpy.context.scene.render.filepath = "output.mp4"
bpy.context.scene.render.resolution_x = 800
bpy.context.scene.render.resolution_y = 600
bpy.context.scene.render.file_format = 'FFMPEG'
bpy.ops.render.render(write_still=False)
