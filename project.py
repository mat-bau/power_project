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


    # code
    b1 = pp.create_bus(net, vn_kv=20, name="Bus 1")
    b2 = pp.create_bus(net, vn_kv=380, name="Bus 2")
    b3 = pp.create_bus(net, vn_kv=150, name="Bus 3")
    b4 = pp.create_bus(net, vn_kv=15, name="Bus 4")
    b5 = pp.create_bus(net, vn_kv=380, name="Bus 5")

    # connect buses
    pp.create_transformer(net, hv_bus=b5, lv_bus=b1, std_type="_20kV_380kV_type", name="Trafo_1_5")
    pp.create_line(net, from_bus=b2, to_bus=b5, length_km=1, std_type="_380kv_type", name="Line_5_2")
    pp.create_transformer(net, hv_bus=b2, lv_bus=b3, std_type="_150kV_380kV_type", name="Trafo_2_3")
    trafo_3_4 = pp.create_transformer(net, hv_bus=b3, lv_bus=b4, std_type="_15kV_150kV_type", name="Trafo_3_4")

    # generator on b1
    pp.create_gen(net, bus=b1, p_mw=650, max_q_mvar=675, min_q_mvar=-250, sn_mva=1000, vm_pu=1, slack=True, name="Generator")

    # load on b1
    pp.create_load(net, bus=b1, p_mw=50, q_mvar=40, name="Load_b1")

    # load on b4
    pp.create_load(net, bus=b4, p_mw=360, q_mvar=180, name="Load_b4")

    # shunts on b3 and b4
    pp.create_shunt(net, bus=b3, q_mvar=-75, p_mw=0, name="Shunt_b3")
    pp.create_shunt(net, bus=b4, q_mvar=-45, p_mw=0, name="Shunt_b4")

    ct.DiscreteTapControl(net, element_index=trafo_3_4, vm_lower_pu=1.01, vm_upper_pu=1.021)


    return net

