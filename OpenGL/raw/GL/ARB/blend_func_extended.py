'''OpenGL extension ARB.blend_func_extended

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_blend_func_extended'
_DEPRECATED = False
GL_SRC1_COLOR = constant.Constant( 'GL_SRC1_COLOR', 0x88F9 )
GL_ONE_MINUS_SRC1_COLOR = constant.Constant( 'GL_ONE_MINUS_SRC1_COLOR', 0x88FA )
GL_ONE_MINUS_SRC1_ALPHA = constant.Constant( 'GL_ONE_MINUS_SRC1_ALPHA', 0x88FB )
GL_MAX_DUAL_SOURCE_DRAW_BUFFERS = constant.Constant( 'GL_MAX_DUAL_SOURCE_DRAW_BUFFERS', 0x88FC )
glBindFragDataLocationIndexed = platform.createExtensionFunction( 
'glBindFragDataLocationIndexed',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLuint,constants.GLuint,arrays.GLcharArray,),
doc='glBindFragDataLocationIndexed(GLuint(program), GLuint(colorNumber), GLuint(index), GLcharArray(name)) -> None',
argNames=('program','colorNumber','index','name',),
deprecated=_DEPRECATED,
)

glGetFragDataIndex = platform.createExtensionFunction( 
'glGetFragDataIndex',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=constants.GLint, 
argTypes=(constants.GLuint,arrays.GLcharArray,),
doc='glGetFragDataIndex(GLuint(program), GLcharArray(name)) -> constants.GLint',
argNames=('program','name',),
deprecated=_DEPRECATED,
)


def glInitBlendFuncExtendedARB():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
