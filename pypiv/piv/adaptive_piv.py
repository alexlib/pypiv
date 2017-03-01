import numpy as np

from velocity_scaler import VelocityUpscaler
from grid_deformator import GridDeformator
from direct_piv import DirectPIV
from grid_spec import GridSpec

class AdaptivePIV(DirectPIV):
    """
    Class for the adaptiv piv.

    After the initial piv is done an adaptiv piv can be performed to minimize the error or to make the grid finer.
    This class inherits from the :doc:`initial class DirectPIV <direct_piv>`.
    Therefore the correlation function is inherited as well as the GridSpec.
    In adition to the inherited grid a new Grid is calculated by deforming the grid with respect to the prior calculated velocities.
    In the case that the new grid is supposed to be finer then the one before, the velocities need to be upscaled.
    """

    def __init__(self, piv_object, window_size, search_size, distance, deformation='forward', ipmethod='bilinear'):
        """
        Initialization as an extension of the super class.

        The initialization of the super class is caled to generate all neccesary GridSpecs and grids.
        Aditional information are the deformation method and the interpolation method.
        
        .. ref on methods ons implemented

        :param DirectPIV piv_object: object of the initial piv
        :param int window_size: size of the interogation window
        :param int search_size: size of the search window
        :param int distance: distance between beginning of the first interogationindow and second
        :param str deformation: deformation method
        :param str ipmethod: interpolation method
        """
        image_a, image_b = np.copy(piv_object.frame_a), np.copy(piv_object.frame_b)

        super(AdaptivePIV, self).__init__(image_a, image_b, window_size,
                                          search_size, distance)

        if self.grid_spec.equal_to(piv_object.grid_spec):
            self.u, self.v = np.copy(piv_object.u), np.copy(piv_object.v)
        else:
            vscaler = VelocityUpscaler(self.grid_spec, piv_object.grid_spec)
            self.u = vscaler.scale_field(piv_object.u)
            self.v = vscaler.scale_field(piv_object.v)
        self._deformation_method = deformation
        self._deform_grid(deformation, ipmethod)

    def _deform_grid(self, deformation_method, ipmethod):
        """
        Deforms the regular grid according to velocity and interpolates image.

        In order to capture more particles flowing in the same direction as indecated by the previosly calculated velocityfield, the grid is deformed and the image corresponding to that grid spot interpolated from the original image.
        This gives a new grid with interpolated particle spots.
        Here two methods are avalable:

        * central:
            Leeds to a half deformation in both directions, forward and backwards.
            This as well leeds to two times the computation of the deformation.
        * forward:
            Leeds to a full deformation in forward direction

        :param str deformation_method: deformation method, mentioned above
        :param str ipmethod: interpolation method passed allong to the interpolator
        """
        distance   = self.grid_spec.distance
        shape_b    = self.grid_spec.get_search_grid_shape()
        if deformation_method == 'central':
            shape_a    = self.grid_spec.get_interogation_grid_shape()

            self.grid_def_a  = GridDeformator(self.frame_a, shape_a, distance, ipmethod)
            self.grid_def_a.set_velocities(-self.u/2, -self.v/2.)

            self.grid_def_b  = GridDeformator(self._padded_fb, shape_b, distance, ipmethod)
            self.grid_def_b.set_velocities(self.u/2., self.v/2.)

        if deformation_method == 'forward':
            self.grid_def_b  = GridDeformator(self._padded_fb, shape_b, distance, ipmethod)
            self.grid_def_b.set_velocities(self.u, self.v)

    def _get_window_frames(self, i, j):
        """
        Function overide in order to include the two different deformation methods.

        Functionality is the same as

        .. automethod:: piv.direct_piv.DirectPIV._get_window_frames

        but in this function, before the window in handed over the deformation is performed for that grid point.
        """
        if self._deformation_method == 'central':
            frame_a = self.grid_def_a.get_frame(i, j)
            frame_b = self.grid_def_b.get_frame(i, j)
        if self._deformation_method == 'forward':
            frame_a = self.grid_a[i, j]
            frame_b = self.grid_def_b.get_frame(i, j)
        return frame_a, frame_b




