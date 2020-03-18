__doc__ = """ Call back functions for rod """
__all__ = ["CallBackBaseClass", "MyCallBack", "ContinuumSnakeCallBack"]


class CallBackBaseClass:
    """
    Base call back class, user has to derive new
    call back classes from this class
    """

    def __init__(self):
        pass

    def make_callback(self, system, time, current_step: int):
        """
        This function will be called every time step, user can
        define which parameters at which time-step to be called back
        in derived call back class
        Parameters
        ----------
        system : system is rod
        time : simulation time
        current_step : current simulation time step

        Returns
        -------

        """
        pass


class MyCallBack(CallBackBaseClass):
    """
    My call back class it is derived from the base call back class.
    This is an example, user can use this class as an example to write
    new call back classes
    """

    def __init__(self, step_skip: int, callback_params):
        CallBackBaseClass.__init__(self)
        self.every = step_skip
        self.callback_params = callback_params

    def make_callback(self, system, time, current_step: int):

        if current_step % self.every == 0:

            self.callback_params["time"].append(time)
            self.callback_params["step"].append(current_step)
            self.callback_params["position"].append(system.position_collection.copy())
            self.callback_params["directors"].append(system.director_collection.copy())
            self.callback_params["velocity"].append(system.velocity_collection.copy())

            return


class ContinuumSnakeCallBack(CallBackBaseClass):
    """
    Call back function for continuum snake
    """

    def __init__(self, step_skip: int, callback_params):
        CallBackBaseClass.__init__(self)
        self.every = step_skip
        self.callback_params = callback_params

    def make_callback(self, system, time, current_step: int):

        if current_step % self.every == 0:

            self.callback_params["time"].append(time)
            self.callback_params["step"].append(current_step)
            self.callback_params["position"].append(system.position_collection.copy())
            self.callback_params["velocity"].append(system.velocity_collection.copy())
            self.callback_params["avg_velocity"].append(
                system.compute_velocity_center_of_mass()
            )

            return
