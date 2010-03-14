'''OpenGL extension VERSION.GL_3_2

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_VERSION_GL_3_2'
_DEPRECATED = False
GL_CONTEXT_CORE_PROFILE_BIT = constant.Constant( 'GL_CONTEXT_CORE_PROFILE_BIT', 0x1 )
GL_CONTEXT_COMPATIBILITY_PROFILE_BIT = constant.Constant( 'GL_CONTEXT_COMPATIBILITY_PROFILE_BIT', 0x2 )
GL_LINES_ADJACENCY = constant.Constant( 'GL_LINES_ADJACENCY', 0xA )
GL_LINE_STRIP_ADJACENCY = constant.Constant( 'GL_LINE_STRIP_ADJACENCY', 0xB )
GL_TRIANGLES_ADJACENCY = constant.Constant( 'GL_TRIANGLES_ADJACENCY', 0xC )
GL_TRIANGLE_STRIP_ADJACENCY = constant.Constant( 'GL_TRIANGLE_STRIP_ADJACENCY', 0xD )
GL_PROGRAM_POINT_SIZE = constant.Constant( 'GL_PROGRAM_POINT_SIZE', 0x8642 )
GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS = constant.Constant( 'GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS', 0x8C29 )
GL_FRAMEBUFFER_ATTACHMENT_LAYERED = constant.Constant( 'GL_FRAMEBUFFER_ATTACHMENT_LAYERED', 0x8DA7 )
GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS = constant.Constant( 'GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS', 0x8DA8 )
GL_GEOMETRY_SHADER = constant.Constant( 'GL_GEOMETRY_SHADER', 0x8DD9 )
GL_GEOMETRY_VERTICES_OUT = constant.Constant( 'GL_GEOMETRY_VERTICES_OUT', 0x8916 )
GL_GEOMETRY_INPUT_TYPE = constant.Constant( 'GL_GEOMETRY_INPUT_TYPE', 0x8917 )
GL_GEOMETRY_OUTPUT_TYPE = constant.Constant( 'GL_GEOMETRY_OUTPUT_TYPE', 0x8918 )
GL_MAX_GEOMETRY_UNIFORM_COMPONENTS = constant.Constant( 'GL_MAX_GEOMETRY_UNIFORM_COMPONENTS', 0x8DDF )
GL_MAX_GEOMETRY_OUTPUT_VERTICES = constant.Constant( 'GL_MAX_GEOMETRY_OUTPUT_VERTICES', 0x8DE0 )
GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS = constant.Constant( 'GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS', 0x8DE1 )
GL_MAX_VERTEX_OUTPUT_COMPONENTS = constant.Constant( 'GL_MAX_VERTEX_OUTPUT_COMPONENTS', 0x9122 )
GL_MAX_GEOMETRY_INPUT_COMPONENTS = constant.Constant( 'GL_MAX_GEOMETRY_INPUT_COMPONENTS', 0x9123 )
GL_MAX_GEOMETRY_OUTPUT_COMPONENTS = constant.Constant( 'GL_MAX_GEOMETRY_OUTPUT_COMPONENTS', 0x9124 )
GL_MAX_FRAGMENT_INPUT_COMPONENTS = constant.Constant( 'GL_MAX_FRAGMENT_INPUT_COMPONENTS', 0x9125 )
GL_CONTEXT_PROFILE_MASK = constant.Constant( 'GL_CONTEXT_PROFILE_MASK', 0x9126 )
glGetInteger64i_v = platform.createExtensionFunction( 
'glGetInteger64i_v',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLuint,arrays.GLint64Array,),
doc='glGetInteger64i_v(GLenum(target), GLuint(index), GLint64Array(data)) -> None',
argNames=('target','index','data',),
deprecated=_DEPRECATED,
)

glGetBufferParameteri64v = platform.createExtensionFunction( 
'glGetBufferParameteri64v',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,arrays.GLint64Array,),
doc='glGetBufferParameteri64v(GLenum(target), GLenum(pname), GLint64Array(params)) -> None',
argNames=('target','pname','params',),
deprecated=_DEPRECATED,
)

glProgramParameteri = platform.createExtensionFunction( 
'glProgramParameteri',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,constants.GLint,),
doc='glProgramParameteri(GLuint(program), GLenum(pname), GLint(value)) -> None',
argNames=('program','pname','value',),
deprecated=_DEPRECATED,
)

glFramebufferTexture = platform.createExtensionFunction( 
'glFramebufferTexture',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,constants.GLuint,constants.GLint,),
doc='glFramebufferTexture(GLenum(target), GLenum(attachment), GLuint(texture), GLint(level)) -> None',
argNames=('target','attachment','texture','level',),
deprecated=_DEPRECATED,
)

