import pytest
import numpy as np

from pyccel.epyccel import epyccel
from modules        import arrays

#==============================================================================
# TEST: 1D ARRAYS OF INT-32
#==============================================================================

def test_array_int32_1d_scalar_add():

    f1 = arrays.array_int32_1d_scalar_add
    f2 = epyccel( f1 )

    x1 = np.array( [1,2,3], dtype=np.int32 )
    x2 = np.copy(x1)
    a = 5

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int32_1d_scalar_sub():

    f1 = arrays.array_int32_1d_scalar_sub
    f2 = epyccel( f1 )

    x1 = np.array( [1,2,3], dtype=np.int32 )
    x2 = np.copy(x1)
    a = 5

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int32_1d_scalar_mul():

    f1 = arrays.array_int32_1d_scalar_mul
    f2 = epyccel( f1 )

    x1 = np.array( [1,2,3], dtype=np.int32 )
    x2 = np.copy(x1)
    a = 5

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int32_1d_scalar_idiv():

    f1 = arrays.array_int32_1d_scalar_idiv
    f2 = epyccel( f1 )

    x1 = np.array( [1,2,3], dtype=np.int32 )
    x2 = np.copy(x1)
    a = 5

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int32_1d_add():

    f1 = arrays.array_int32_1d_add
    f2 = epyccel( f1 )

    x1 = np.array( [1,2,3], dtype=np.int32 )
    x2 = np.copy(x1)
    a  = np.array( [1,2,3], dtype=np.int32 )

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int32_1d_sub():

    f1 = arrays.array_int32_1d_sub
    f2 = epyccel( f1 )

    x1 = np.array( [1,2,3], dtype=np.int32 )
    x2 = np.copy(x1)
    a  = np.array( [1,2,3], dtype=np.int32 )

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int32_1d_mul():

    f1 = arrays.array_int32_1d_mul
    f2 = epyccel( f1 )

    x1 = np.array( [1,2,3], dtype=np.int32 )
    x2 = np.copy(x1)
    a  = np.array( [1,2,3], dtype=np.int32 )

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int32_1d_idiv():

    f1 = arrays.array_int32_1d_idiv
    f2 = epyccel( f1 )

    x1 = np.array( [1,2,3], dtype=np.int32 )
    x2 = np.copy(x1)
    a  = np.array( [1,2,3], dtype=np.int32 )

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

#==============================================================================
# TEST: 2D ARRAYS OF INT-32 WITH C ORDERING
#==============================================================================

def test_array_int32_2d_C_scalar_add():

    f1 = arrays.array_int32_2d_C_scalar_add
    f2 = epyccel( f1 )

    x1 = np.array( [[1,2,3], [4,5,6]], dtype=np.int32 )
    x2 = np.copy(x1)
    a = 5

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int32_2d_C_scalar_sub():

    f1 = arrays.array_int32_2d_C_scalar_sub
    f2 = epyccel( f1 )

    x1 = np.array( [[1,2,3], [4,5,6]], dtype=np.int32 )
    x2 = np.copy(x1)
    a = 5

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int32_2d_C_scalar_mul():

    f1 = arrays.array_int32_2d_C_scalar_mul
    f2 = epyccel( f1 )

    x1 = np.array( [[1,2,3], [4,5,6]], dtype=np.int32 )
    x2 = np.copy(x1)
    a = 5

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int32_2d_C_scalar_idiv():

    f1 = arrays.array_int32_2d_C_scalar_idiv
    f2 = epyccel( f1 )

    x1 = np.array( [[1,2,3], [4,5,6]], dtype=np.int32 )
    x2 = np.copy(x1)
    a = 5

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int32_2d_C_add():

    f1 = arrays.array_int32_2d_C_add
    f2 = epyccel( f1 )

    x1 = np.array( [[1,2,3], [4,5,6]], dtype=np.int32 )
    x2 = np.copy(x1)
    a  = np.array( [[-1,-2,-3], [-4,-5,-6]], dtype=np.int32 )

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int32_2d_C_sub():

    f1 = arrays.array_int32_2d_C_sub
    f2 = epyccel( f1 )

    x1 = np.array( [[1,2,3], [4,5,6]], dtype=np.int32 )
    x2 = np.copy(x1)
    a  = np.array( [[-1,-2,-3], [-4,-5,-6]], dtype=np.int32 )

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int32_2d_C_mul():

    f1 = arrays.array_int32_2d_C_mul
    f2 = epyccel( f1 )

    x1 = np.array( [[1,2,3], [4,5,6]], dtype=np.int32 )
    x2 = np.copy(x1)
    a  = np.array( [[-1,-2,-3], [-4,-5,-6]], dtype=np.int32 )

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int32_2d_C_idiv():

    f1 = arrays.array_int32_2d_C_idiv
    f2 = epyccel( f1 )

    x1 = np.array( [[1,2,3], [4,5,6]], dtype=np.int32 )
    x2 = np.copy(x1)
    a  = np.array( [[-1,-2,-3], [-4,-5,-6]], dtype=np.int32 )

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

#==============================================================================
# TEST: 2D ARRAYS OF INT-32 WITH F ORDERING
#==============================================================================

def test_array_int32_2d_F_scalar_add():

    f1 = arrays.array_int32_2d_F_scalar_add
    f2 = epyccel( f1 )

    x1 = np.array( [[1,2,3], [4,5,6]], dtype=np.int32, order='F' )
    x2 = np.copy(x1)
    a = 5

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int32_2d_F_scalar_sub():

    f1 = arrays.array_int32_2d_F_scalar_sub
    f2 = epyccel( f1 )

    x1 = np.array( [[1,2,3], [4,5,6]], dtype=np.int32, order='F' )
    x2 = np.copy(x1)
    a = 5

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int32_2d_F_scalar_mul():

    f1 = arrays.array_int32_2d_F_scalar_mul
    f2 = epyccel( f1 )

    x1 = np.array( [[1,2,3], [4,5,6]], dtype=np.int32, order='F' )
    x2 = np.copy(x1)
    a = 5

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int32_2d_F_scalar_idiv():

    f1 = arrays.array_int32_2d_F_scalar_idiv
    f2 = epyccel( f1 )

    x1 = np.array( [[1,2,3], [4,5,6]], dtype=np.int32, order='F' )
    x2 = np.copy(x1)
    a = 5

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int32_2d_F_add():

    f1 = arrays.array_int32_2d_F_add
    f2 = epyccel( f1 )

    x1 = np.array( [[1,2,3], [4,5,6]], dtype=np.int32, order='F' )
    x2 = np.copy(x1)
    a  = np.array( [[-1,-2,-3], [-4,-5,-6]], dtype=np.int32, order='F' )

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int32_2d_F_sub():

    f1 = arrays.array_int32_2d_F_sub
    f2 = epyccel( f1 )

    x1 = np.array( [[1,2,3], [4,5,6]], dtype=np.int32, order='F' )
    x2 = np.copy(x1)
    a  = np.array( [[-1,-2,-3], [-4,-5,-6]], dtype=np.int32, order='F' )

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int32_2d_F_mul():

    f1 = arrays.array_int32_2d_F_mul
    f2 = epyccel( f1 )

    x1 = np.array( [[1,2,3], [4,5,6]], dtype=np.int32, order='F' )
    x2 = np.copy(x1)
    a  = np.array( [[-1,-2,-3], [-4,-5,-6]], dtype=np.int32, order='F' )

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int32_2d_F_idiv():

    f1 = arrays.array_int32_2d_F_idiv
    f2 = epyccel( f1 )

    x1 = np.array( [[1,2,3], [4,5,6]], dtype=np.int32, order='F' )
    x2 = np.copy(x1)
    a  = np.array( [[-1,-2,-3], [-4,-5,-6]], dtype=np.int32, order='F' )

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )


#==============================================================================
# TEST: 1D ARRAYS OF INT-64
#==============================================================================

def test_array_int_1d_scalar_add():

    f1 = arrays.array_int_1d_scalar_add
    f2 = epyccel( f1 )

    x1 = np.array( [1,2,3] )
    x2 = np.copy(x1)
    a = 5

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int_1d_scalar_sub():

    f1 = arrays.array_int_1d_scalar_sub
    f2 = epyccel( f1 )

    x1 = np.array( [1,2,3] )
    x2 = np.copy(x1)
    a = 5

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int_1d_scalar_mul():

    f1 = arrays.array_int_1d_scalar_mul
    f2 = epyccel( f1 )

    x1 = np.array( [1,2,3] )
    x2 = np.copy(x1)
    a = 5

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int_1d_scalar_idiv():

    f1 = arrays.array_int_1d_scalar_idiv
    f2 = epyccel( f1 )

    x1 = np.array( [1,2,3] )
    x2 = np.copy(x1)
    a = 5

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int_1d_add():

    f1 = arrays.array_int_1d_add
    f2 = epyccel( f1 )

    x1 = np.array( [1,2,3] )
    x2 = np.copy(x1)
    a  = np.array( [1,2,3] )

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int_1d_sub():

    f1 = arrays.array_int_1d_sub
    f2 = epyccel( f1 )

    x1 = np.array( [1,2,3] )
    x2 = np.copy(x1)
    a  = np.array( [1,2,3] )

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int_1d_mul():

    f1 = arrays.array_int_1d_mul
    f2 = epyccel( f1 )

    x1 = np.array( [1,2,3] )
    x2 = np.copy(x1)
    a  = np.array( [1,2,3] )

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int_1d_idiv():

    f1 = arrays.array_int_1d_idiv
    f2 = epyccel( f1 )

    x1 = np.array( [1,2,3] )
    x2 = np.copy(x1)
    a  = np.array( [1,2,3] )

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

#==============================================================================
# TEST: 2D ARRAYS OF INT-64 WITH C ORDERING
#==============================================================================

def test_array_int_2d_C_scalar_add():

    f1 = arrays.array_int_2d_C_scalar_add
    f2 = epyccel( f1 )

    x1 = np.array( [[1,2,3], [4,5,6]] )
    x2 = np.copy(x1)
    a = 5

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int_2d_C_scalar_sub():

    f1 = arrays.array_int_2d_C_scalar_sub
    f2 = epyccel( f1 )

    x1 = np.array( [[1,2,3], [4,5,6]] )
    x2 = np.copy(x1)
    a = 5

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int_2d_C_scalar_mul():

    f1 = arrays.array_int_2d_C_scalar_mul
    f2 = epyccel( f1 )

    x1 = np.array( [[1,2,3], [4,5,6]] )
    x2 = np.copy(x1)
    a = 5

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int_2d_C_scalar_idiv():

    f1 = arrays.array_int_2d_C_scalar_idiv
    f2 = epyccel( f1 )

    x1 = np.array( [[1,2,3], [4,5,6]] )
    x2 = np.copy(x1)
    a = 5

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int_2d_C_add():

    f1 = arrays.array_int_2d_C_add
    f2 = epyccel( f1 )

    x1 = np.array( [[1,2,3], [4,5,6]] )
    x2 = np.copy(x1)
    a  = np.array( [[-1,-2,-3], [-4,-5,-6]] )

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int_2d_C_sub():

    f1 = arrays.array_int_2d_C_sub
    f2 = epyccel( f1 )

    x1 = np.array( [[1,2,3], [4,5,6]] )
    x2 = np.copy(x1)
    a  = np.array( [[-1,-2,-3], [-4,-5,-6]] )

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int_2d_C_mul():

    f1 = arrays.array_int_2d_C_mul
    f2 = epyccel( f1 )

    x1 = np.array( [[1,2,3], [4,5,6]] )
    x2 = np.copy(x1)
    a  = np.array( [[-1,-2,-3], [-4,-5,-6]] )

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int_2d_C_idiv():

    f1 = arrays.array_int_2d_C_idiv
    f2 = epyccel( f1 )

    x1 = np.array( [[1,2,3], [4,5,6]] )
    x2 = np.copy(x1)
    a  = np.array( [[-1,-2,-3], [-4,-5,-6]] )

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int_2d_C_initialization():

    f1 = arrays.array_int_2d_C_initialization
    f2 = epyccel(f1)

    x1 = np.zeros((2, 3), dtype=int)
    x2 = np.ones_like(x1)

    f1(x1)
    f2(x2)

    assert np.array_equal(x1, x2)

#==============================================================================
# TEST: 2D ARRAYS OF INT-64 WITH F ORDERING
#==============================================================================

def test_array_int_2d_F_scalar_add():

    f1 = arrays.array_int_2d_F_scalar_add
    f2 = epyccel( f1 )

    x1 = np.array( [[1,2,3], [4,5,6]], order='F' )
    x2 = np.copy(x1)
    a = 5

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int_2d_F_scalar_sub():

    f1 = arrays.array_int_2d_F_scalar_sub
    f2 = epyccel( f1 )

    x1 = np.array( [[1,2,3], [4,5,6]], order='F' )
    x2 = np.copy(x1)
    a = 5

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int_2d_F_scalar_mul():

    f1 = arrays.array_int_2d_F_scalar_mul
    f2 = epyccel( f1 )

    x1 = np.array( [[1,2,3], [4,5,6]], order='F' )
    x2 = np.copy(x1)
    a = 5

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int_2d_F_scalar_idiv():

    f1 = arrays.array_int_2d_F_scalar_idiv
    f2 = epyccel( f1 )

    x1 = np.array( [[1,2,3], [4,5,6]], order='F' )
    x2 = np.copy(x1)
    a = 5

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int_2d_F_add():

    f1 = arrays.array_int_2d_F_add
    f2 = epyccel( f1 )

    x1 = np.array( [[1,2,3], [4,5,6]], order='F' )
    x2 = np.copy(x1)
    a  = np.array( [[-1,-2,-3], [-4,-5,-6]], order='F' )

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int_2d_F_sub():

    f1 = arrays.array_int_2d_F_sub
    f2 = epyccel( f1 )

    x1 = np.array( [[1,2,3], [4,5,6]], order='F' )
    x2 = np.copy(x1)
    a  = np.array( [[-1,-2,-3], [-4,-5,-6]], order='F' )

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int_2d_F_mul():

    f1 = arrays.array_int_2d_F_mul
    f2 = epyccel( f1 )

    x1 = np.array( [[1,2,3], [4,5,6]], order='F' )
    x2 = np.copy(x1)
    a  = np.array( [[-1,-2,-3], [-4,-5,-6]], order='F' )

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int_2d_F_idiv():

    f1 = arrays.array_int_2d_F_idiv
    f2 = epyccel( f1 )

    x1 = np.array( [[1,2,3], [4,5,6]], order='F' )
    x2 = np.copy(x1)
    a  = np.array( [[-1,-2,-3], [-4,-5,-6]], order='F' )

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_int_2d_F_initialization():

    f1 = arrays.array_int_2d_F_initialization
    f2 = epyccel(f1)

    x1 = np.zeros((2, 3), dtype=int, order='F')
    x2 = np.ones_like(x1)

    f1(x1)
    f2(x2)

    assert np.array_equal(x1, x2)

#==============================================================================
# TEST: 1D ARRAYS OF REAL
#==============================================================================

def test_array_real_1d_scalar_add():

    f1 = arrays.array_real_1d_scalar_add
    f2 = epyccel( f1 )

    x1 = np.array( [1.,2.,3.] )
    x2 = np.copy(x1)
    a = 5.

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_real_1d_scalar_sub():

    f1 = arrays.array_real_1d_scalar_sub
    f2 = epyccel( f1 )

    x1 = np.array( [1.,2.,3.] )
    x2 = np.copy(x1)
    a = 5.

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_real_1d_scalar_mul():

    f1 = arrays.array_real_1d_scalar_mul
    f2 = epyccel( f1 )

    x1 = np.array( [1.,2.,3.] )
    x2 = np.copy(x1)
    a = 5.

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_real_1d_scalar_div():

    f1 = arrays.array_real_1d_scalar_div
    f2 = epyccel( f1 )

    x1 = np.array( [1.,2.,3.] )
    x2 = np.copy(x1)
    a = 5.

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_real_1d_add():

    f1 = arrays.array_real_1d_add
    f2 = epyccel( f1 )

    x1 = np.array( [1.,2.,3.] )
    x2 = np.copy(x1)
    a  = np.array( [1.,2.,3.] )

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_real_1d_sub():

    f1 = arrays.array_real_1d_sub
    f2 = epyccel( f1 )

    x1 = np.array( [1.,2.,3.] )
    x2 = np.copy(x1)
    a  = np.array( [1.,2.,3.] )

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_real_1d_mul():

    f1 = arrays.array_real_1d_mul
    f2 = epyccel( f1 )

    x1 = np.array( [1.,2.,3.] )
    x2 = np.copy(x1)
    a  = np.array( [1.,2.,3.] )

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_real_1d_div():

    f1 = arrays.array_real_1d_div
    f2 = epyccel( f1 )

    x1 = np.array( [1.,2.,3.] )
    x2 = np.copy(x1)
    a  = np.array( [1.,2.,3.] )

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

#==============================================================================
# TEST: 2D ARRAYS OF REAL WITH C ORDERING
#==============================================================================

def test_array_real_2d_C_scalar_add():

    f1 = arrays.array_real_2d_C_scalar_add
    f2 = epyccel( f1 )

    x1 = np.array( [[1.,2.,3.], [4.,5.,6.]] )
    x2 = np.copy(x1)
    a = 5.

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_real_2d_C_scalar_sub():

    f1 = arrays.array_real_2d_C_scalar_sub
    f2 = epyccel( f1 )

    x1 = np.array( [[1.,2.,3.], [4.,5.,6.]] )
    x2 = np.copy(x1)
    a = 5.

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_real_2d_C_scalar_mul():

    f1 = arrays.array_real_2d_C_scalar_mul
    f2 = epyccel( f1 )

    x1 = np.array( [[1.,2.,3.], [4.,5.,6.]] )
    x2 = np.copy(x1)
    a = 5.

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_real_2d_C_scalar_div():

    f1 = arrays.array_real_2d_C_scalar_div
    f2 = epyccel( f1 )

    x1 = np.array( [[1.,2.,3.], [4.,5.,6.]] )
    x2 = np.copy(x1)
    a = 5.

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_real_2d_C_add():

    f1 = arrays.array_real_2d_C_add
    f2 = epyccel( f1 )

    x1 = np.array( [[1.,2.,3.], [4.,5.,6.]] )
    x2 = np.copy(x1)
    a  = np.array( [[-1.,-2.,-3.], [-4.,-5.,-6.]] )

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_real_2d_C_sub():

    f1 = arrays.array_real_2d_C_sub
    f2 = epyccel( f1 )

    x1 = np.array( [[1.,2.,3.], [4.,5.,6.]] )
    x2 = np.copy(x1)
    a  = np.array( [[-1.,-2.,-3.], [-4.,-5.,-6.]] )

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_real_2d_C_mul():

    f1 = arrays.array_real_2d_C_mul
    f2 = epyccel( f1 )

    x1 = np.array( [[1.,2.,3.], [4.,5.,6.]] )
    x2 = np.copy(x1)
    a  = np.array( [[-1.,-2.,-3.], [-4.,-5.,-6.]] )

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_real_2d_C_div():

    f1 = arrays.array_real_2d_C_div
    f2 = epyccel( f1 )

    x1 = np.array( [[1.,2.,3.], [4.,5.,6.]] )
    x2 = np.copy(x1)
    a  = np.array( [[-1.,-2.,-3.], [-4.,-5.,-6.]] )

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_real_2d_C_initialization():

    f1 = arrays.array_real_2d_C_initialization
    f2 = epyccel(f1)

    x1 = np.zeros((2, 3), dtype=float )
    x2 = np.ones_like(x1)

    f1(x1)
    f2(x2)

    assert np.array_equal(x1, x2)

#==============================================================================
# TEST: 2D ARRAYS OF REAL WITH F ORDERING
#==============================================================================

def test_array_real_2d_F_scalar_add():

    f1 = arrays.array_real_2d_F_scalar_add
    f2 = epyccel( f1 )

    x1 = np.array( [[1.,2.,3.], [4.,5.,6.]], order='F' )
    x2 = np.copy(x1)
    a = 5.

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_real_2d_F_scalar_sub():

    f1 = arrays.array_real_2d_F_scalar_sub
    f2 = epyccel( f1 )

    x1 = np.array( [[1.,2.,3.], [4.,5.,6.]], order='F' )
    x2 = np.copy(x1)
    a = 5.

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_real_2d_F_scalar_mul():

    f1 = arrays.array_real_2d_F_scalar_mul
    f2 = epyccel( f1 )

    x1 = np.array( [[1.,2.,3.], [4.,5.,6.]], order='F' )
    x2 = np.copy(x1)
    a = 5.

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_real_2d_F_scalar_div():

    f1 = arrays.array_real_2d_F_scalar_div
    f2 = epyccel( f1 )

    x1 = np.array( [[1.,2.,3.], [4.,5.,6.]], order='F' )
    x2 = np.copy(x1)
    a = 5.

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_real_2d_F_add():

    f1 = arrays.array_real_2d_F_add
    f2 = epyccel( f1 )

    x1 = np.array( [[1.,2.,3.], [4.,5.,6.]], order='F' )
    x2 = np.copy(x1)
    a  = np.array( [[-1.,-2.,-3.], [-4.,-5.,-6.]], order='F' )

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_real_2d_F_sub():

    f1 = arrays.array_real_2d_F_sub
    f2 = epyccel( f1 )

    x1 = np.array( [[1.,2.,3.], [4.,5.,6.]], order='F' )
    x2 = np.copy(x1)
    a  = np.array( [[-1.,-2.,-3.], [-4.,-5.,-6.]], order='F' )

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_real_2d_F_mul():

    f1 = arrays.array_real_2d_F_mul
    f2 = epyccel( f1 )

    x1 = np.array( [[1.,2.,3.], [4.,5.,6.]], order='F' )
    x2 = np.copy(x1)
    a  = np.array( [[-1.,-2.,-3.], [-4.,-5.,-6.]], order='F' )

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_real_2d_F_div():

    f1 = arrays.array_real_2d_F_div
    f2 = epyccel( f1 )

    x1 = np.array( [[1.,2.,3.], [4.,5.,6.]], order='F' )
    x2 = np.copy(x1)
    a  = np.array( [[-1.,-2.,-3.], [-4.,-5.,-6.]], order='F' )

    f1(x1, a)
    f2(x2, a)

    assert np.array_equal( x1, x2 )

def test_array_real_2d_F_initialization():

    f1 = arrays.array_real_2d_F_initialization
    f2 = epyccel(f1)

    x1 = np.zeros((2, 3), dtype=float, order='F')
    x2 = np.ones_like(x1)

    f1(x1)
    f2(x2)

    assert np.array_equal(x1, x2)

#==============================================================================
# TEST: 1D Stack ARRAYS OF REAL
#==============================================================================

def test_array_real_sum_stack_array():

    f1 = arrays.array_real_1d_sum_stack_array
    f2 = epyccel( f1 )
    x1 = f1()
    x2 = f2()
    assert np.equal( x1, x2 )

def test_array_real_div_stack_array():

    f1 = arrays.array_real_1d_div_stack_array
    f2 = epyccel( f1 )
    x1 = f1()
    x2 = f2()
    assert np.equal( x1, x2 )

#==============================================================================
# TEST: Product and matrix multiplication
#==============================================================================
def test_array_real_1d_1d_prod():
    f1 = arrays.array_real_1d_1d_prod
    f2 = epyccel( f1 )
    x1 = np.array([3.0, 2.0, 1.0])
    x2 = np.copy(x1)
    y1 = np.empty(3)
    y2 = np.empty(3)
    f1(x1, y1)
    f2(x2, y2)
    assert np.array_equal(y1, y2)

def test_array_real_2d_1d_matmul():
    f1 = arrays.array_real_2d_1d_matmul
    f2 = epyccel( f1 )
    A1 = np.ones([3, 2])
    A1[1,0] = 2
    A2 = np.copy(A1)
    x1 = np.ones([2, 1])
    x2 = np.copy(x1)
    y1 = np.empty([3,1])
    y2 = np.empty([3,1])
    f1(A1, x1, y1)
    f2(A2, x2, y2)
    assert np.array_equal(y1, y2)

def test_array_real_2d_1d_matmul_order_C_F():
    f1 = arrays.array_real_2d_1d_matmul
    f2 = epyccel( f1 )
    A1 = np.ones([3, 2], order='F')
    A1[1,0] = 2
    A2 = np.copy(A1)
    x1 = np.ones([2, 1])
    x2 = np.copy(x1)
    y1 = np.empty([3, 1])
    y2 = np.empty([3, 1])
    f1(A1, x1, y1)
    f2(A2, x2, y2)
    assert np.array_equal(y1, y2)

def test_array_real_1d_2d_matmul_order_F():
    f1 = arrays.array_real_1d_2d_matmul
    f2 = epyccel( f1 )
    A1 = np.ones([3, 2], order='F')
    A1[1, 0] = 2
    A2 = np.copy(A1)
    x1 = np.ones([1, 3])
    x2 = np.copy(x1)
    y1 = np.empty(2)
    y2 = np.empty(2)
    f1(x1, A1, y1)
    f2(x2, A2, y2)
    assert np.array_equal(y1, y2)

def test_array_real_2d_1d_matmul_order_F_C():
    f1 = arrays.array_real_2d_1d_matmul_order_F
    f2 = epyccel( f1 )
    A1 = np.ones([3, 2])
    A1[1,0] = 2
    A2 = np.copy(A1)
    x1 = np.ones([2, 1])
    x2 = np.copy(x1)
    y1 = np.empty([3, 1])
    y2 = np.empty([3, 1])
    f1(A1, x1, y1)
    f2(A2, x2, y2)
    assert np.array_equal(y1, y2)

def test_array_real_2d_1d_matmul_order_F_F():
    f1 = arrays.array_real_2d_1d_matmul_order_F
    f2 = epyccel( f1 )
    A1 = np.ones([3, 2], order='F')
    A1[1,0] = 2
    A2 = np.copy(A1)
    x1 = np.ones([2, 1])
    x2 = np.copy(x1)
    y1 = np.empty([3, 1])
    y2 = np.empty([3, 1])
    f1(A1, x1, y1)
    f2(A2, x2, y2)
    assert np.array_equal(y1, y2)

def test_array_real_2d_2d_matmul():
    f1 = arrays.array_real_2d_2d_matmul
    f2 = epyccel( f1 )
    A1 = np.ones([3, 2])
    A1[1, 0] = 2
    A2 = np.copy(A1)
    B1 = np.ones([2, 3])
    B2 = np.copy(B1)
    C1 = np.empty([3,3])
    C2 = np.empty([3,3])
    f1(A1, B1, C1)
    f2(A2, B2, C2)
    assert np.array_equal(C1, C2)

def test_array_real_2d_2d_matmul_C_C_F_F():
    f1 = arrays.array_real_2d_2d_matmul
    f2 = epyccel( f1 )
    A1 = np.ones([3, 2], order='F')
    A1[1, 0] = 2
    A2 = np.copy(A1)
    B1 = np.ones([2, 3], order='F')
    B2 = np.copy(B1)
    C1 = np.empty([3,3])
    C2 = np.empty([3,3])
    f1(A1, B1, C1)
    f2(A2, B2, C2)
    assert np.array_equal(C1, C2)

def test_array_real_2d_2d_matmul_C_C_C_F():
    f1 = arrays.array_real_2d_2d_matmul
    f2 = epyccel( f1 )
    A1 = np.ones([3, 2])
    A1[1, 0] = 2
    A2 = np.copy(A1)
    B1 = np.ones([2, 3], order='F')
    B2 = np.copy(B1)
    C1 = np.empty([3,3])
    C2 = np.empty([3,3])
    f1(A1, B1, C1)
    f2(A2, B2, C2)
    assert np.array_equal(C1, C2)

def test_array_real_2d_2d_matmul_F_F_F_F():
    f1 = arrays.array_real_2d_2d_matmul_F_F
    f2 = epyccel( f1 )
    A1 = np.ones([3, 2], order='F')
    A1[1, 0] = 2
    A2 = np.copy(A1)
    B1 = np.ones([2, 3], order='F')
    B2 = np.copy(B1)
    C1 = np.empty([3,3], order='F')
    C2 = np.empty([3,3], order='F')
    f1(A1, B1, C1)
    f2(A2, B2, C2)
    assert np.array_equal(C1, C2)

@pytest.mark.xfail(reason="Should fail as long as mixed order not supported, see #244")
def test_array_real_2d_2d_matmul_mixorder():
    f1 = arrays.array_real_2d_2d_matmul_mixorder
    f2 = epyccel( f1 )
    A1 = np.ones([3, 2])
    A1[1, 0] = 2
    A2 = np.copy(A1)
    B1 = np.ones([2, 3])
    B2 = np.copy(B1)
    C1 = np.empty([3,3])
    C2 = np.empty([3,3])
    f1(A1, B1, C1)
    f2(A2, B2, C2)
    assert np.array_equal(C1, C2)

# TODO: Fix #245
@pytest.mark.xfail(reason="Needs fixing, see #245")
def test_array_real_loopdiff():
    f1 = arrays.array_real_loopdiff
    f2 = epyccel( f1 )
    x1 = np.ones(5)
    y1 = np.zeros(5)
    x2 = np.copy(x1)
    y2 = np.copy(y1)
    z1 = np.empty(5)
    z2 = np.empty(5)
    f1(x1, y1, z1)
    f2(x2, y2, z2)
    assert np.array_equal(z1, z2)

##==============================================================================
## CLEAN UP GENERATED FILES AFTER RUNNING TESTS
##==============================================================================
#
#def teardown_module():
#    import os, glob
#    dirname  = os.path.dirname( arrays.__file__ )
#    pattern  = os.path.join( dirname, '__epyccel__*' )
#    filelist = glob.glob( pattern )
#    for f in filelist:
#        os.remove( f )
