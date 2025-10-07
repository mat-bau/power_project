import pandapower as pp
import pandapower.control as ct


def My_Amazing_Grid():

    net = pp.create_empty_network(f_hz=50, sn_mva=100)
    # Custom transformer types
    pp.create_std_type(net, {"sn_mva": 1000.0, "vn_hv_kv": 380.0, "vn_lv_kv": 20.0, "vk_percent": 10.0, "vkr_percent": 0.2, "pfe_kw": 0, "i0_percent": 0.0, "shift_degree": 0.0, "tap_side": "hv", "tap_neutral": 0, "tap_min": -20, "tap_max": 20, "tap_step_percent": 1, "tap_step_degree": 0, "tap_phase_shifter": False}, name="_20kV_380kV_type", element='trafo')
    pp.create_std_type(net, {"sn_mva": 550.0, "vn_hv_kv": 380.0, "vn_lv_kv": 150.0, "vk_percent": 22.0, "vkr_percent": 0.25, "pfe_kw": 0, "i0_percent": 0.0, "shift_degree": 0.0, "tap_side": "hv", "tap_neutral": 0, "tap_min": -20, "tap_max": 20, "tap_step_percent": 1, "tap_step_degree": 0, "tap_phase_shifter": False}, name="_150kV_380kV_type", element='trafo')
    pp.create_std_type(net, {"sn_mva": 500.0, "vn_hv_kv": 150.0, "vn_lv_kv": 15.0, "vk_percent": 12.0, "vkr_percent": 0.28, "pfe_kw": 0, "i0_percent": 0.0, "shift_degree": 0.0, "tap_side": "lv", "tap_neutral": 0, "tap_min": -4, "tap_max": 20, "tap_step_percent": 1.0, "tap_step_degree": 0, "tap_phase_shifter": False}, name="_15kV_150kV_type", element='trafo')
    pp.create_std_type(net, {"sn_mva": 500.0, "vn_hv_kv": 150.0, "vn_lv_kv": 20.0, "vk_percent": 13.0, "vkr_percent": 0.25, "pfe_kw": 0, "i0_percent": 0.0, "shift_degree": 0.0, "tap_side": "hv", "tap_neutral": 0, "tap_min": -20, "tap_max": 20, "tap_step_percent": 1, "tap_step_degree": 0, "tap_phase_shifter": False}, name="_20kV_150kV_type", element='trafo')

    # Custom line types
    pp.create_std_type(net, {"c_nf_per_km": 500.0, "r_ohm_per_km": 1.2, "x_ohm_per_km": 12, "max_i_ka": 2.15}, name="_380kv_type", element='line')
    pp.create_std_type(net, {"c_nf_per_km": 150.0, "r_ohm_per_km": 1.4, "x_ohm_per_km": 9, "max_i_ka": 1.35}, name="_150kv_type", element='line')

    # Respect the following conventions: (DO NOT CHANGE | BEGIN)

    # If there is a problem with the code, it's a good idea to start by checking if the code follows the conventions here below.

    # Use the following nomenclature for the ID’s elements and names.
    # Bx (with x a number) for buses
    # LOAD_Bx for load connected to Bx
    # C_Bx for shunts to Bx
    # LINE_BxBy for line between Bx and By with x<y
    # TRAFO_BxBy for transformer between Bx and By with x<y
    # G_Bx for generator connected to Bx
    # No need for transformers’ controllers
    # /!\ If several elements are in parallel, follow this : LINE_BxBy_1, LINE_BxBy_2, LINE_BxBy_3 and so on.

    # Loads’ information
    # Here is the consumption profile of the loads associated to their buses in MW/MVar.
    # (P,Q) = (50,40) for B1, B7
    # (P,Q) = (200,50) for B27,B30,B32, B34
    # (P,Q) = (360,180) for B4,B11,B14,B16,B18,B22, B26

    # Shunts’ information 
    # Here is the production profile of the shunts associated to their buses in MVar.
    # (Q) = (75) for B3, B8, B19, B21, B25
    # (Q) = (45) for B4, B11, B14, B16, B18, B22, B26

    # Lines’ information
    # Use the relevant standard type for the lines.
    # Choose 1km line length (unrealistic but easier for pedagogical reasons)
    # From_bus : Bx
    # To_bus : By
    # With x<y

    # Transformers’ information
    # Use the relevant standard Type for the transformers (see Inginious).
    # Control, in a discrete way, the 150kV/15kV transformers.
    # The voltage has to be controlled between 1.01 and 1.021 pu.

    # Generators’ information
    # For B1, B7: (P, Qmax, Qmin, Sn, v_pu, slack) = (650, 675, -250, 1000, 1, 0)
    # For B12, B15, B20: (P, Qmax, Qmin, Sn, v_pu, slack) = (300, 200, -50, 450, .98, 0)
    # For B29: (P, Qmax, Qmin, Sn, v_pu, slack) = (800, 575, -250, 1000, 1.09, 1)
    # For B31, B33 : (P, Qmax, Qmin, Sn, v_pu, slack) = (210, 2000, -500, 1000, 1.09, 0)
    # By default, all the quantities are in Mega unless it is explicitily written down.

    # (DO NOT CHANGE | END)

    # Do not forget to follow the relevant indentation when you submit
    

    # Grid 1 - Tilmans



    # Grid 2 - Scupp



    # Grid 3 - Bauvir


    #  Grid 4 - Tilmans


    #   Grid 5 - Schupp


    return net