import bpy
from Sollumz.sollumz_properties import BoundType, PolygonType, SOLLUMZ_UI_NAMES, is_sollum_type
from Sollumz.meshhelper import * 
from .collision_materials import create_collision_material_from_index, create_collision_material_from_type
from .properties import BoundFlags

def load_default_flags(obj):
    obj.composite_flags1['map_weapon'] = True
    obj.composite_flags1['map_dynamic'] = True
    obj.composite_flags1['map_animal'] = True
    obj.composite_flags1['map_vehicle'] = True
    obj.composite_flags1['map_cover'] = True

    for flag_name in BoundFlags.__annotations__.keys():
        obj.composite_flags2[flag_name] = True

def create_empty(sollum_type):
    empty = bpy.data.objects.new(SOLLUMZ_UI_NAMES[sollum_type], None)
    empty.empty_display_size = 0
    empty.sollum_type = sollum_type
    bpy.context.collection.objects.link(empty)
    bpy.context.view_layer.objects.active = bpy.data.objects[empty.name]

    return empty

def create_mesh(sollum_type):
    name = SOLLUMZ_UI_NAMES[sollum_type]
    mesh = bpy.data.meshes.new(name)
    obj = bpy.data.objects.new(name, mesh)
    obj.sollum_type = sollum_type
    bpy.context.collection.objects.link(obj)

    return obj

def aobj_is_composite(self, sollum_type):
    aobj = bpy.context.active_object
    if not (aobj and aobj.sollum_type == BoundType.COMPOSITE):
        self.report({'INFO'}, f"Please select a {SOLLUMZ_UI_NAMES[BoundType.COMPOSITE]} to add a {SOLLUMZ_UI_NAMES[sollum_type]} to.")
        return False
    return True

class SOLLUMZ_OT_create_bound_composite(bpy.types.Operator):
    """Create a sollumz bound composite"""
    bl_idname = "sollumz.createboundcomposite"
    bl_label = f"Create {SOLLUMZ_UI_NAMES[BoundType.COMPOSITE]}"

    def execute(self, context):
        
        create_empty(BoundType.COMPOSITE)

        return {'FINISHED'}


class SOLLUMZ_OT_create_geometry_bound(bpy.types.Operator):
    """Create a sollumz geometry bound"""
    bl_idname = "sollumz.creategeometrybound"
    bl_label = f"Create {SOLLUMZ_UI_NAMES[BoundType.GEOMETRY]}"

    def execute(self, context):
        if not aobj_is_composite(self, BoundType.GEOMETRY):
            return {'CANCELLED'}

        aobj = bpy.context.active_object
        gobj = create_empty(BoundType.GEOMETRY)
        gobj.parent = aobj
        bpy.context.view_layer.objects.active = bpy.data.objects[gobj.name]

        return {'FINISHED'}


class SOLLUMZ_OT_create_geometrybvh_bound(bpy.types.Operator):
    """Create a sollumz geometry bound bvh"""
    bl_idname = "sollumz.creategeometryboundbvh"
    bl_label = f"Create {SOLLUMZ_UI_NAMES[BoundType.GEOMETRYBVH]}"

    def execute(self, context):
        if not aobj_is_composite(self, BoundType.GEOMETRYBVH):
            return {'CANCELLED'}
        
        aobj = bpy.context.active_object
        gobj = create_empty(BoundType.GEOMETRYBVH) 
        gobj.parent = aobj
        bpy.context.view_layer.objects.active = bpy.data.objects[gobj.name]

        return {'FINISHED'}


class SOLLUMZ_OT_create_box_bound(bpy.types.Operator):
    """Create a sollumz box bound"""
    bl_idname = "sollumz.createboxbound"
    bl_label = f"Create {SOLLUMZ_UI_NAMES[BoundType.BOX]}"

    def execute(self, context):
        if not aobj_is_composite(self, BoundType.BOX):
            return {'CANCELLED'}
        
        aobj = bpy.context.active_object
        gobj = create_mesh(BoundType.BOX)
        create_box(gobj.data)
        gobj.parent = aobj
        bpy.context.view_layer.objects.active = bpy.data.objects[gobj.name]

        return {'FINISHED'}


class SOLLUMZ_OT_create_sphere_bound(bpy.types.Operator):
    """Create a sollumz sphere bound"""
    bl_idname = "sollumz.createspherebound"
    bl_label = f"Create {SOLLUMZ_UI_NAMES[BoundType.SPHERE]}"

    def execute(self, context):
        if not aobj_is_composite(self, BoundType.SPHERE):
            return {'CANCELLED'}
        
        aobj = bpy.context.active_object
        gobj = create_mesh(BoundType.SPHERE)
        create_sphere(gobj.data)
        gobj.parent = aobj
        bpy.context.view_layer.objects.active = bpy.data.objects[gobj.name]
            

        return {'FINISHED'}


class SOLLUMZ_OT_create_capsule_bound(bpy.types.Operator):
    """Create a sollumz capsule bound"""
    bl_idname = "sollumz.createcapsulebound"
    bl_label = f"Create {SOLLUMZ_UI_NAMES[BoundType.CAPSULE]}"

    def execute(self, context):
        if not aobj_is_composite(self, BoundType.CAPSULE):
            return {'CANCELLED'}
        
        aobj = bpy.context.active_object
        gobj = create_mesh(BoundType.CAPSULE)
        create_capsule(gobj)
        gobj.parent = aobj
        bpy.context.view_layer.objects.active = bpy.data.objects[gobj.name]

        return {'FINISHED'}


class SOLLUMZ_OT_create_cylinder_bound(bpy.types.Operator):
    """Create a sollumz cylinder bound"""
    bl_idname = "sollumz.createcylinderbound"
    bl_label = f"Create {SOLLUMZ_UI_NAMES[BoundType.CYLINDER]}"

    def execute(self, context):
        if not aobj_is_composite(self, BoundType.CYLINDER):
            return {'CANCELLED'}
        
        aobj = bpy.context.active_object
        gobj = create_mesh(BoundType.CYLINDER)
        create_cylinder(gobj.data)
        gobj.parent = aobj
        bpy.context.view_layer.objects.active = bpy.data.objects[gobj.name]

        return {'FINISHED'}


class SOLLUMZ_OT_create_disc_bound(bpy.types.Operator):
    """Create a sollumz disc bound"""
    bl_idname = "sollumz.creatediscbound"
    bl_label = f"Create {SOLLUMZ_UI_NAMES[BoundType.DISC]}"

    def execute(self, context):
        if not aobj_is_composite(self, BoundType.DISC):
            return {'CANCELLED'}
        
        aobj = bpy.context.active_object
        gobj = create_mesh(BoundType.DISC)
        create_disc(gobj.data)
        gobj.parent = aobj
        bpy.context.view_layer.objects.active = bpy.data.objects[gobj.name]

        return {'FINISHED'}


class SOLLUMZ_OT_create_cloth_bound(bpy.types.Operator):
    """Create a sollumz cloth bound"""
    bl_idname = "sollumz.createclothbound"
    bl_label = f"Create {SOLLUMZ_UI_NAMES[BoundType.CLOTH]}"

    def execute(self, context):
        if not aobj_is_composite(self, BoundType.CLOTH):
            return {'CANCELLED'}
        
        aobj = bpy.context.active_object
        gobj = create_empty(BoundType.CLOTH)
        gobj.parent = aobj
        bpy.context.view_layer.objects.active = bpy.data.objects[gobj.name]

        return {'FINISHED'}


class SOLLUMZ_OT_create_polygon_bound(bpy.types.Operator):
    """Create a sollumz polygon bound"""
    bl_idname = "sollumz.createpolygonbound"
    bl_label = "Create Polygon Bound"

    def execute(self, context):
        aobj = bpy.context.active_object
        type = context.scene.poly_bound_type

        if not (aobj and (aobj.sollum_type == BoundType.GEOMETRY or aobj.sollum_type == BoundType.GEOMETRYBVH)):
            self.report({'INFO'}, f"Please select a {SOLLUMZ_UI_NAMES[BoundType.GEOMETRYBVH]} or {SOLLUMZ_UI_NAMES[BoundType.GEOMETRY]} to add a {SOLLUMZ_UI_NAMES[type]} to.")
            return {'CANCELLED'}
        
        pobj = create_mesh(type)

        if type == PolygonType.BOX:
            create_box(pobj.data)
        elif type == PolygonType.SPHERE:
            create_sphere(pobj.data)
        elif type == PolygonType.CAPSULE:
            create_capsule(pobj)
        elif type == PolygonType.CYLINDER:
            create_cylinder(pobj.data)

        pobj.parent = aobj
        #bpy.context.view_layer.objects.active = bpy.data.objects[cobj.name] if you enable this you wont be able to stay selecting the composite obj... 

        return {'FINISHED'}


class SOLLUMZ_OT_create_collision_material(bpy.types.Operator):
    """Create a sollumz collision material"""
    bl_idname = "sollumz.createcollisionmaterial"
    bl_label = "Create Collision Material"

    def execute(self, context):
        
        aobj = bpy.context.active_object
        if(aobj == None):
            return {'CANCELLED'}
        
        if is_sollum_type(aobj, PolygonType):
            mat = create_collision_material_from_index(context.scene.collision_material_index)
            aobj.data.materials.append(mat)
        
        return {'FINISHED'}


class SOLLUMZ_OT_load_default_col_flags(bpy.types.Operator):
    """Load commonly used collision flags"""
    bl_idname = "sollumz.load_default_col_flags"
    bl_label = "Load Default Collision Flags"

    def execute(self, context):
        
        aobj = bpy.context.active_object
        if(aobj == None):
            return {'CANCELLED'}
        
        load_default_flags(aobj)
        
        return {'FINISHED'}


class SOLLUMZ_OT_clear_col_flags(bpy.types.Operator):
    """Load commonly used collision flags"""
    bl_idname = "sollumz.clear_col_flags"
    bl_label = "Clear Collision Flags"

    def execute(self, context):
        
        aobj = bpy.context.active_object
        if(aobj == None):
            return {'CANCELLED'}
        
        if is_sollum_type(aobj, BoundType):
            for flag_name in BoundFlags.__annotations__.keys():
                aobj.composite_flags1[flag_name] = False
                aobj.composite_flags2[flag_name] = False
        
        return {'FINISHED'}


class SOLLUMZ_OT_mesh_to_polygon_bound(bpy.types.Operator):
    """Convert selected objects to a poly bound"""
    bl_idname = "sollumz.meshtopolygonbound"
    bl_label = "Convert Object to Poly"
    bl_options = {'UNDO'}

    def execute(self, context):
        aobj = context.active_object
        type = context.scene.convert_poly_bound_type
        parent = context.scene.convert_poly_parent


        if not aobj or (aobj and not aobj.type == 'MESH'):
            self.report({'WARNING'}, 'No object with mesh data selected!')
            return {'CANCELLED'}
        elif aobj and not context.active_object.mode == 'EDIT':
            self.report({'WARNING'}, 'Operator can only be ran in edit mode!')
            return {'CANCELLED'}
        
        if not parent:
            self.report({'WARNING'}, 'Must specify a parent object!')
            return {'CANCELLED'}
        elif parent.sollum_type != BoundType.GEOMETRYBVH and parent.sollum_type != BoundType.GEOMETRY:
            self.report({'WARNING'}, f'Parent must be a {SOLLUMZ_UI_NAMES[BoundType.GEOMETRYBVH]} or {SOLLUMZ_UI_NAMES[BoundType.GEOMETRY]}!')
            return {'CANCELLED'}

        # We need to switch from Edit mode to Object mode so the vertex selection gets updated (disgusting!)
        bpy.ops.object.mode_set(mode='OBJECT')
        selected_verts = [Vector((v.co.x, v.co.y, v.co.z)) for v in aobj.data.vertices if v.select]
        bpy.ops.object.mode_set(mode='EDIT')


        if len(selected_verts) < 1:
            self.report({'INFO'}, 'No vertices selected.')
            return {'CANCELLED'}

        pobj = create_mesh(type)

        np_array = np.array(selected_verts)
        bbmin_local = Vector(np_array.min(axis=0))
        bbmax_local = Vector(np_array.max(axis=0))
        bbmin = aobj.matrix_world @ bbmin_local
        bbmax = aobj.matrix_world @ bbmax_local

        radius = ((aobj.matrix_local @ bbmax).x - (aobj.matrix_local @ bbmin).x) / 2
        height = get_distance_of_vectors(bbmin, bbmax)
        center = (bbmin + bbmax) / 2
        pobj.location = center

        if type == PolygonType.BOX:
            scale = aobj.matrix_world.to_scale()
            min = (bbmin_local) * scale
            max = (bbmax_local) * scale
            center = (min + max) / 2
            create_box_from_extents(pobj.data, min - center, max - center)
            # pobj.location = Vector()
        elif type == PolygonType.SPHERE:
            create_sphere(pobj.data, height / 2)
        elif type == PolygonType.CAPSULE or type == PolygonType.CYLINDER:
            if type == PolygonType.CAPSULE:
                # height = height - (radius * 2)
                create_capsule(pobj, radius, height)
            elif type == PolygonType.CYLINDER:
                create_cylinder(pobj.data, radius, height, False)
        
        pobj.rotation_euler = aobj.rotation_euler
        
        pobj.parent = parent

        return {'FINISHED'}


class SOLLUMZ_OT_convert_mesh_to_collision(bpy.types.Operator):
    """Setup a gta bound via a mesh object"""
    bl_idname = "sollumz.quickconvertmeshtocollision"
    bl_label = "Convert Mesh To Collision"

    def convert(self, obj):
        #create material
        mat = create_collision_material_from_type("DEFAULT")
        obj.data.materials.append(mat)
        
        #set parents
        bpy.ops.sollumz.createboundcomposite()
        bobj = bpy.context.active_object
        bpy.ops.sollumz.creategeometryboundbvh()
        gobj = bpy.context.active_object
        gobj.parent = bobj
        obj.parent = gobj

        #set properties
        obj.sollum_type = PolygonType.TRIANGLE.value

    def execute(self, context):
        
        for obj in context.selected_objects:
            self.convert(obj)

        return {'FINISHED'}