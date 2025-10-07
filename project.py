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


    # Your code goes here
    # Do not forget to follow the relevant indentation when you submit


    return net