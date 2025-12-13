import pandapower as pp 
from pandapower.control.controller.trafo.ContinuousTapControl import ContinuousTapControl
import pandapower.topology as top
import pandapower.plotting as plot
from pandapower.plotting.plotly import pf_res_plotly
from pandapower.plotting.plotly import simple_plotly
import pandapower.control as ct
import numpy as np
net = pp.create_empty_network(f_hz=50, sn_mva=100)
    
vmin = 0.95
vmax = 1.1
load_max = 100.

    
# list of Buses
M1 = pp.create_bus(net, vn_kv=20.0, name="M1", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (1.5,4))
M2 = pp.create_bus(net, vn_kv=20.0, name="M2", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (3,4))
M3 = pp.create_bus(net, vn_kv=20.0, name="M3", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (0,0))
M4 = pp.create_bus(net, vn_kv=20.0, name="M4", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (4,0))
M5 = pp.create_bus(net, vn_kv=20.0, name="M5", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (4.5,-3))
M6 = pp.create_bus(net, vn_kv=20.0, name="M6", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (1,-5))
N11 = pp.create_bus(net, vn_kv=380.0, name="N11", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (0,-4))
N8 = pp.create_bus(net, vn_kv=380.0, name="N8", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (0.5,-3))
N9 = pp.create_bus(net, vn_kv=380.0, name="N9", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (1,-3))
N10 = pp.create_bus(net, vn_kv=380.0, name="N10", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (1,-4))
N13 = pp.create_bus(net, vn_kv=380.0, name="N13", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (5,-4))
N104 = pp.create_bus(net, vn_kv=150.0, name="N104", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (2,-2))
N203 = pp.create_bus(net, vn_kv=15.0, name="N203", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (2,-3))
N206 = pp.create_bus(net, vn_kv=15.0, name="N206", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (6,0))
N102 = pp.create_bus(net, vn_kv=150.0, name="N102", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (2,1))
N202 = pp.create_bus(net, vn_kv=15.0, name="N202", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (2,0))
N105 = pp.create_bus(net, vn_kv=150.0, name="N105", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (5,-2))
N205 = pp.create_bus(net, vn_kv=15.0, name="N205", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (5.5,-3))
N101 = pp.create_bus(net, vn_kv=150.0, name="N101", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (0.5,1))
N201 = pp.create_bus(net, vn_kv=15.0, name="N201", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (1,0))
N107 = pp.create_bus(net, vn_kv=150.0, name="N107", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (8,1))
N207 = pp.create_bus(net, vn_kv=15.0, name="N207", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (8,0))
N204 = pp.create_bus(net, vn_kv=15.0, name="N204", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (5,0))
N12 = pp.create_bus(net, vn_kv=380.0, name="N12", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (0,-3))
N6 = pp.create_bus(net, vn_kv=380.0, name="N6", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (1.5,-1))
N4 = pp.create_bus(net, vn_kv=380.0, name="N4", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (2.5,2))
N7 = pp.create_bus(net, vn_kv=380.0, name="N7", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (4.5,-1))
N1 = pp.create_bus(net, vn_kv=380.0, name="N1", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (2.5,3))
N2 = pp.create_bus(net, vn_kv=380.0, name="N2", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (8,2))
N3 = pp.create_bus(net, vn_kv=380.0, name="N3", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (0.5,2))
N5 = pp.create_bus(net, vn_kv=380.0, name="N5", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (6,2))
N103 = pp.create_bus(net, vn_kv=150.0, name="N103", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (4.5,1))
N106 = pp.create_bus(net, vn_kv=150.0, name="N106", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (6,1))
N14 = pp.create_bus(net, vn_kv=380.0, name="N14", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (6,-4))


# list of Loads:
LOAD_M1 = pp.create_load(net, bus=M1, p_mw=50.0, q_mvar=40.0, name="M1", in_service=True, max_p_mw=50., min_p_mw=50.0, max_q_mvar=40., min_q_mvar=40., controllable = True)
LOAD_M2 = pp.create_load(net, bus=M2, p_mw=50.0, q_mvar=40.0, name="M2", in_service=True, max_p_mw=50.0, min_p_mw=50.0, max_q_mvar=40., min_q_mvar=40., controllable = True)
LOAD_N11 = pp.create_load(net, bus=N11, p_mw=100.0, q_mvar=30.0, name="N11", in_service=True, max_p_mw=100., min_p_mw=100., max_q_mvar=30., min_q_mvar=30., controllable = True)
LOAD_N8 = pp.create_load(net, bus=N8, p_mw=230.0, q_mvar=75.0, name="N8", in_service=True, max_p_mw=230., min_p_mw=230., max_q_mvar=75., min_q_mvar=75., controllable = True)
LOAD_N9 = pp.create_load(net, bus=N9, p_mw=220.0, q_mvar=70.0, name="N9", in_service=True, max_p_mw=220., min_p_mw=220., max_q_mvar=70., min_q_mvar=70., controllable = True)
LOAD_N13 = pp.create_load(net, bus=N13, p_mw=300.0, q_mvar=75.0, name="N13", in_service=True, max_p_mw=300., min_p_mw=300., max_q_mvar=75., min_q_mvar=75., controllable = True)
LOAD_N203 = pp.create_load(net, bus=N203, p_mw=360.0, q_mvar=180.0, name="N203", in_service=True, max_p_mw=540., min_p_mw=360., max_q_mvar=180., min_q_mvar=180., controllable = True)
LOAD_N206 = pp.create_load(net, bus=N206, p_mw=360.0, q_mvar=180.0, name="N206", in_service=True, max_p_mw=360., min_p_mw=360., max_q_mvar=180., min_q_mvar=180., controllable = True)
LOAD_N202 = pp.create_load(net, bus=N202, p_mw=360.0, q_mvar=180.0, name="N202", in_service=True, max_p_mw=360., min_p_mw=360., max_q_mvar=180., min_q_mvar=180., controllable = True)
LOAD_N205 = pp.create_load(net, bus=N205, p_mw=360.0, q_mvar=180.0, name="N205", in_service=True, max_p_mw=360., min_p_mw=360., max_q_mvar=180., min_q_mvar=180., controllable = True)
LOAD_N201 = pp.create_load(net, bus=N201, p_mw=360.0, q_mvar=180.0, name="N201", in_service=True, max_p_mw=360., min_p_mw=360., max_q_mvar=180., min_q_mvar=180., controllable = True)
LOAD_N207 = pp.create_load(net, bus=N207, p_mw=360.0, q_mvar=180.0, name="N207", in_service=True, max_p_mw=360., min_p_mw=360., max_q_mvar=180., min_q_mvar=180., controllable = True)
LOAD_N204 = pp.create_load(net, bus=N204, p_mw=360.0, q_mvar=180.0, name="N204", in_service=True, max_p_mw=360., min_p_mw=360., max_q_mvar=180., min_q_mvar=180., controllable = True)




# List of Shunts:
pp.create_shunt(net, bus=N104, q_mvar=-75.0, in_service=True)
pp.create_shunt(net, bus=N203, q_mvar=-45.0, in_service=True)
pp.create_shunt(net, bus=N206, q_mvar=-45.0, in_service=True)
pp.create_shunt(net, bus=N102, q_mvar=-75.0, in_service=True)
pp.create_shunt(net, bus=N202, q_mvar=-45.0, in_service=True)
pp.create_shunt(net, bus=N105, q_mvar=-75.0, in_service=True)
pp.create_shunt(net, bus=N205, q_mvar=-45.0, in_service=True)
pp.create_shunt(net, bus=N101, q_mvar=-75.0, in_service=True)
pp.create_shunt(net, bus=N201, q_mvar=-45.0, in_service=True)
pp.create_shunt(net, bus=N107, q_mvar=-75.0, in_service=True)
pp.create_shunt(net, bus=N207, q_mvar=-45.0, in_service=True)
pp.create_shunt(net, bus=N204, q_mvar=-45.0, in_service=True)


# list of Lines
pp.create_line_from_parameters(net, from_bus= N11, to_bus= N10, name="'N11N10", length_km=1, r_ohm_per_km=1.141, x_ohm_per_km=12.086, max_i_ka=2.157467, c_nf_per_km=434.703079165756, in_service=True,max_loading_percent = load_max , controllable = True, geodata = [(0,-4),(1,-4)])
pp.create_line_from_parameters(net, from_bus= N6, to_bus= N8, name="'N6N8", length_km=1, r_ohm_per_km=1.444, x_ohm_per_km=14.44, max_i_ka=2.157467, c_nf_per_km=537.867313277922, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(1.5,-1),(0.5,-3)])
pp.create_line_from_parameters(net, from_bus= N6, to_bus= N9, name="'N6N9", length_km=1, r_ohm_per_km=1.357, x_ohm_per_km=14.368, max_i_ka=2.157467, c_nf_per_km=538.306580920856, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(1.5,-1),(1,-3)])
pp.create_line_from_parameters(net, from_bus= N6, to_bus= N4, name="'N6N4", length_km=1, r_ohm_per_km=1.213, x_ohm_per_km=10.224, max_i_ka=2.157467, c_nf_per_km=380.915074598419, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(1.5,-1),(1.5,1.5),(2.5,2)])
pp.create_line_from_parameters(net, from_bus= N6, to_bus= N7, name="'N6N7", length_km=1, r_ohm_per_km=1.213, x_ohm_per_km=10.224, max_i_ka=2.157467, c_nf_per_km=380.915074598419, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(1.5,-1),(4.5,-1)])
pp.create_line_from_parameters(net, from_bus= N8, to_bus= N10, name="'N8N10", length_km=1, r_ohm_per_km=2.166, x_ohm_per_km=23.104, max_i_ka=2.157467, c_nf_per_km=881.718384729100, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(0.5,-3),(1,-4)])
pp.create_line_from_parameters(net, from_bus= N9, to_bus= N10, name="'N9N10", length_km=1, r_ohm_per_km=2.166, x_ohm_per_km=23.104, max_i_ka=2.157467, c_nf_per_km=881.718384729100, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(1,-3),(1,-4)])
pp.create_line_from_parameters(net, from_bus= N1, to_bus= N4, name="'N1N41", length_km=1, r_ohm_per_km=0.765, x_ohm_per_km=6.7, max_i_ka=2.051113, c_nf_per_km=249.975119817855, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(2.5,3),(2.5,2.5),(2.5,2)])
pp.create_line_from_parameters(net, from_bus= N1, to_bus= N4, name="'N1N42", length_km=1, r_ohm_per_km=0.708, x_ohm_per_km=7.538, max_i_ka=2.051113, c_nf_per_km=282.601883151693, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(2.5,3),(2.25,2.5),(2.5,2)])
pp.create_line_from_parameters(net, from_bus= N1, to_bus= N4, name="'N1N43", length_km=1, r_ohm_per_km=0.708, x_ohm_per_km=7.538, max_i_ka=2.051113, c_nf_per_km=282.601883151693, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(2.5,3),(2.75,2.5),(2.5,2)])
pp.create_line_from_parameters(net, from_bus= N1, to_bus= N2, name="'N1N2", length_km=1, r_ohm_per_km=0.202, x_ohm_per_km=2.094, max_i_ka=2.157467, c_nf_per_km=71.422372261919, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(2.5,3),(8,2)])
pp.create_line_from_parameters(net, from_bus= N10, to_bus= N13, name="'N10N13", length_km=1, r_ohm_per_km=1.256, x_ohm_per_km=13.992, max_i_ka=2.157467, c_nf_per_km=510.091592609524, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(1,-4),(5,-4)])
pp.create_line_from_parameters(net, from_bus= N4, to_bus= N3, name="'N4N3", length_km=1, r_ohm_per_km=1.054, x_ohm_per_km=11.148, max_i_ka=2.157467, c_nf_per_km=417.947246757041, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(2.5,2),(0.5,2)])
pp.create_line_from_parameters(net, from_bus= N5, to_bus= N4, name="'N5N41", length_km=1, r_ohm_per_km=0.664, x_ohm_per_km=7.076, max_i_ka=2.157467, c_nf_per_km=240.273034486973, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(6,2),(4.25,2.25),(2.5,2)])
pp.create_line_from_parameters(net, from_bus= N5, to_bus= N4, name="'N5N42", length_km=1, r_ohm_per_km=0.664, x_ohm_per_km=7.076, max_i_ka=2.157467, c_nf_per_km=240.273034486973, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(6,2),(4.25,1.75),(2.5,2)])
pp.create_line_from_parameters(net, from_bus= N102, to_bus= N103, name="'N102N103", length_km=1, r_ohm_per_km=0.225, x_ohm_per_km=2.565, max_i_ka=1.347151, c_nf_per_km=56.589131565754, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(2,1),(4.5,1)])
pp.create_line_from_parameters(net, from_bus= N102, to_bus= N101, name="'N102N101", length_km=1, r_ohm_per_km=3.825, x_ohm_per_km=14.218, max_i_ka=1.347151, c_nf_per_km=325.382731854794, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(2,1),(0.5,1)])
pp.create_line_from_parameters(net, from_bus= N106, to_bus= N103, name="'N106N103", length_km=1, r_ohm_per_km=1.237, x_ohm_per_km=5.625, max_i_ka=1.347151, c_nf_per_km=113.178263131509, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(6,1),(4.5,1)])
pp.create_line_from_parameters(net, from_bus= N106, to_bus= N105, name="'N106N105", length_km=1, r_ohm_per_km=1.8, x_ohm_per_km=9.675, max_i_ka=1.347151, c_nf_per_km=198.058777381278, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(6,1),(5,-2)])
pp.create_line_from_parameters(net, from_bus= N104, to_bus= N105, name="'N104N105", length_km=1, r_ohm_per_km=1.395, x_ohm_per_km=6.75, max_i_ka=1.347151, c_nf_per_km=141.469645815524, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(2,-2),(5,-2)])
pp.create_line_from_parameters(net, from_bus= N104, to_bus= N103, name="'N104N103", length_km=1, r_ohm_per_km=1.395, x_ohm_per_km=6.75, max_i_ka=1.347151, c_nf_per_km=141.469645815524, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(2,-2),(4.5,1)])
pp.create_line_from_parameters(net, from_bus= N13, to_bus= N14, name="'N13N14", length_km=1, r_ohm_per_km=3.148, x_ohm_per_km=33.342, max_i_ka=2.051113, c_nf_per_km=636.180504724648, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(5,-4),(6,-4)])
pp.create_line_from_parameters(net, from_bus= N11, to_bus= N12, name="'N11N12", length_km=1, r_ohm_per_km=1.819, x_ohm_per_km=19.22, max_i_ka=2.051113, c_nf_per_km=597.384895796567, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(0,-4),(0,-3)])

# list of Transformers:
pp.create_transformer_from_parameters(net, hv_bus=N2, lv_bus=N107, sn_mva=550.0, name='N2N107', shift_degree=0.0, vn_hv_kv=380.0, vn_lv_kv=150.0, vkr_percent=0.312, vk_percent=22.72114224681497, pfe_kw=0, i0_percent=0.0, tap_min=-20, tap_max=20, tap_step_percent=1, tap_pos=8,tap_neutral=0, tap_side="hv", in_service=True,max_loading_percent = load_max)
pp.create_transformer_from_parameters(net, hv_bus=N3, lv_bus=N101, sn_mva=550.0, name='N3N101', shift_degree=0.0, vn_hv_kv=380.0, vn_lv_kv=150.0, vkr_percent=0.26, vk_percent=22.621494203522456, pfe_kw=0, i0_percent=0.0, tap_min=-20, tap_max=20, tap_step_percent=1, tap_pos=3,tap_neutral=0, tap_side="hv", in_service=True,max_loading_percent = load_max)
pp.create_transformer_from_parameters(net, hv_bus=N7, lv_bus=N105, sn_mva=550.0, name='N7N105', shift_degree=0.0, vn_hv_kv=380.0, vn_lv_kv=150.0, vkr_percent=0.26, vk_percent=22.621494203522456, pfe_kw=0, i0_percent=0.0, tap_min=-20, tap_max=20, tap_step_percent=1, tap_pos=7,tap_neutral=0, tap_side="hv", in_service=True,max_loading_percent = load_max)
pp.create_transformer_from_parameters(net, hv_bus=N4, lv_bus=N102, sn_mva=550.0, name='N4N102', shift_degree=0.0, vn_hv_kv=380.0, vn_lv_kv=150.0, vkr_percent=0.416, vk_percent=24.542525888750735, pfe_kw=0, i0_percent=0.0, tap_min=-20, tap_max=20, tap_step_percent=1, tap_pos=14,tap_neutral=0, tap_side="hv", in_service=True,max_loading_percent = load_max)
pp.create_transformer_from_parameters(net, hv_bus=N5, lv_bus=N106, sn_mva=550.0, name='N5N106', shift_degree=0.0, vn_hv_kv=380.0, vn_lv_kv=150.0, vkr_percent=0.151, vk_percent=11.596983099065032, pfe_kw=0, i0_percent=0.0, tap_min=-20, tap_max=20, tap_step_percent=1, tap_pos=6,tap_neutral=0, tap_side="hv", in_service=True,max_loading_percent = load_max)
pp.create_transformer_from_parameters(net, hv_bus=N6, lv_bus=N104, sn_mva=550.0, name='N6N104', shift_degree=0.0, vn_hv_kv=380.0, vn_lv_kv=150.0, vkr_percent=0.146, vk_percent=11.440931605424446, pfe_kw=0, i0_percent=0.0, tap_min=-20, tap_max=20, tap_step_percent=1, tap_pos=2,tap_neutral=0, tap_side="hv", in_service=True,max_loading_percent = load_max)
pp.create_transformer_from_parameters(net, hv_bus=N1, lv_bus=M1, sn_mva=1000.0, name='M1N1', shift_degree=0.0, vn_hv_kv=380.0, vn_lv_kv=20.0, vkr_percent=0.23, vk_percent=10.702471677140752, pfe_kw=0, i0_percent=0.0, tap_min=-20, tap_max=20, tap_step_percent=1, tap_pos=8,tap_neutral=0, tap_side="hv", in_service=True,max_loading_percent = load_max)
pp.create_transformer_from_parameters(net, hv_bus=N1, lv_bus=M2, sn_mva=1000.0, name='M2N1', shift_degree=0.0, vn_hv_kv=380.0, vn_lv_kv=20.0, vkr_percent=0.117, vk_percent=9.854694566550501, pfe_kw=0, i0_percent=0.0, tap_min=-20, tap_max=20, tap_step_percent=1, tap_pos=6,tap_neutral=0, tap_side="hv", in_service=True,max_loading_percent = load_max)
pp.create_transformer_from_parameters(net, hv_bus=N10, lv_bus=M6, sn_mva=1000.0, name='M6N10', shift_degree=0.0, vn_hv_kv=380.0, vn_lv_kv=20.0, vkr_percent=0.25, vk_percent=13.002403623945844, pfe_kw=0, i0_percent=0.0, tap_min=-20, tap_max=20, tap_step_percent=1, tap_pos=10,tap_neutral=0, tap_side="hv", in_service=True,max_loading_percent = load_max)
pp.create_transformer_from_parameters(net, hv_bus=N105, lv_bus=M5, sn_mva=500.0, name='M5N105', shift_degree=0.0, vn_hv_kv=150.0, vn_lv_kv=20.0, vkr_percent=0.25, vk_percent=13.002403623945844, pfe_kw=0, i0_percent=0.0, tap_min=-20, tap_max=20, tap_step_percent=1, tap_pos=10,tap_neutral=0, tap_side="hv", in_service=True,max_loading_percent = load_max)
pp.create_transformer_from_parameters(net, hv_bus=N101, lv_bus=M3, sn_mva=500.0, name='M3N101', shift_degree=0.0, vn_hv_kv=150.0, vn_lv_kv=20.0, vkr_percent=0.25, vk_percent=13.002403623945844, pfe_kw=0, i0_percent=0.0, tap_min=-20, tap_max=20, tap_step_percent=1, tap_pos=10,tap_neutral=0, tap_side="hv", in_service=True,max_loading_percent = load_max)
pp.create_transformer_from_parameters(net, hv_bus=N103, lv_bus=M4, sn_mva=350.0, name='M4N103', shift_degree=0.0, vn_hv_kv=150.0, vn_lv_kv=20.0, vkr_percent=0.25, vk_percent=13.002403623945844, pfe_kw=0, i0_percent=0.0, tap_min=-20, tap_max=20, tap_step_percent=1, tap_pos=10,tap_neutral=0, tap_side="hv", in_service=True,max_loading_percent = load_max)
pp.create_transformer_from_parameters(net, hv_bus=N101, lv_bus=N201, sn_mva=500.0, name="'N201N101'", vn_hv_kv=150.0, vn_lv_kv=15.0, vkr_percent=0.277, vk_percent=11.53832544176147, pfe_kw=0, i0_percent=0.0, tap_pos=0, tap_neutral=0, tap_step_percent=1.0, tap_side="lv", tap_min=-4, tap_max=20, in_service=True,max_loading_percent = load_max)
pp.create_transformer_from_parameters(net, hv_bus=N102, lv_bus=N202, sn_mva=500.0, name="'N202N102'", vn_hv_kv=150.0, vn_lv_kv=15.0, vkr_percent=0.271, vk_percent=11.298250572544406, pfe_kw=0, i0_percent=0.0, tap_pos=0, tap_neutral=0, tap_step_percent=1.0, tap_side="lv", tap_min=-4, tap_max=20, in_service=True,max_loading_percent = load_max)
pp.create_transformer_from_parameters(net, hv_bus=N104, lv_bus=N203, sn_mva=500.0, name="'N203N104'", vn_hv_kv=150.0, vn_lv_kv=15.0, vkr_percent=0.271, vk_percent=11.298250572544406, pfe_kw=0, i0_percent=0.0, tap_pos=0, tap_neutral=0, tap_step_percent=1.0, tap_side="lv", tap_min=-4, tap_max=20, in_service=True,max_loading_percent = load_max)
pp.create_transformer_from_parameters(net, hv_bus=N103, lv_bus=N204, sn_mva=500.0, name="'N204N103'", vn_hv_kv=150.0, vn_lv_kv=15.0, vkr_percent=0.277, vk_percent=11.53832544176147, pfe_kw=0, i0_percent=0.0, tap_pos=0, tap_neutral=0, tap_step_percent=1.0, tap_side="lv", tap_min=-4, tap_max=20, in_service=True,max_loading_percent = load_max)
pp.create_transformer_from_parameters(net, hv_bus=N105, lv_bus=N205, sn_mva=500.0, name="'N205N105'", vn_hv_kv=150.0, vn_lv_kv=15.0, vkr_percent=0.283, vk_percent=11.785398296196867, pfe_kw=0, i0_percent=0.0, tap_pos=0, tap_neutral=0, tap_step_percent=1.0, tap_side="lv", tap_min=-4, tap_max=20, in_service=True,max_loading_percent = load_max)
pp.create_transformer_from_parameters(net, hv_bus=N106, lv_bus=N206, sn_mva=500.0, name="'N206N106'", vn_hv_kv=150.0, vn_lv_kv=15.0, vkr_percent=0.277, vk_percent=11.53832544176147, pfe_kw=0, i0_percent=0.0, tap_pos=0, tap_neutral=0, tap_step_percent=1.0, tap_side="lv", tap_min=-4, tap_max=20, in_service=True,max_loading_percent = load_max)
pp.create_transformer_from_parameters(net, hv_bus=N107, lv_bus=N207, sn_mva=500.0, name="'N207N107'", vn_hv_kv=150.0, vn_lv_kv=15.0, vkr_percent=0.277, vk_percent=11.53832544176147, pfe_kw=0, i0_percent=0.0, tap_pos=0, tap_neutral=0, tap_step_percent=1.0, tap_side="lv", tap_min=-4, tap_max=20, in_service=True,max_loading_percent = load_max)

# list of Generators:
G1 = pp.create_gen(net, p_mw=700.0, max_q_mvar=638.58, min_q_mvar=-250.0, sn_mva=1000.0, bus=M1, vm_pu=0.99958, name="M1", slack=False, in_service=True, min_p_mw=0., max_p_mw=850., controllable = True)
G2 = pp.create_gen(net, p_mw=600.0, max_q_mvar=696.53, min_q_mvar=-250.0, sn_mva=1000.0, bus=M2, vm_pu=0.99958, name="M2", slack=False, in_service=True, min_p_mw=0., max_p_mw=850., controllable = True)
G3=pp.create_gen(net, p_mw=375.0, max_q_mvar=220.83, min_q_mvar=-50.0, sn_mva=450.00, bus=M3, vm_pu=0.99000, name="M3", slack=False, in_service=True, min_p_mw=0., max_p_mw=405., controllable = True)
G4=pp.create_gen(net, p_mw=250.0, max_q_mvar=143.76, min_q_mvar=-50.0, sn_mva=300.00, bus=M4, vm_pu=0.97580, name="M4", slack=False, in_service=True, min_p_mw=0., max_p_mw=270., controllable = True)
G5=pp.create_gen(net, p_mw=375.0, max_q_mvar=220.97, min_q_mvar=-50.0, sn_mva=450.00, bus=M5, vm_pu=0.99040, name="M5", slack=False, in_service=True, min_p_mw=0., max_p_mw=405., controllable = True)
G6=pp.create_gen(net, p_mw=804.0, max_q_mvar=572.16, min_q_mvar=-250.0, sn_mva=1000.0, bus=M6, vm_pu=1.0100, name="M6", slack=True, in_service=True, min_p_mw=0., max_p_mw=850., controllable = True)
G7=pp.create_gen(net, p_mw=255.0, max_q_mvar=9999.0, min_q_mvar=-999.0, sn_mva=1000.0, bus=N12, vm_pu=1.0994, name="N12", slack=False, in_service=True, min_p_mw=0., max_p_mw=5000., controllable = True)
G8=pp.create_gen(net, p_mw=174.0, max_q_mvar=9999.0, min_q_mvar=-999.0, sn_mva=1000.0, bus=N14, vm_pu=1.0929, name="N14", slack=False, in_service=True, min_p_mw=0., max_p_mw=2450., controllable = True)

# Controllers :
ct.controller.trafo.DiscreteTapControl.DiscreteTapControl(net,12, 1.01,1.021, order = 0)
ct.controller.trafo.DiscreteTapControl.DiscreteTapControl(net,13, 1.01,1.021, order = 0)
ct.controller.trafo.DiscreteTapControl.DiscreteTapControl(net,14, 1.01,1.021, order = 0)
ct.controller.trafo.DiscreteTapControl.DiscreteTapControl(net,15, 1.01,1.021, order = 0)
ct.controller.trafo.DiscreteTapControl.DiscreteTapControl(net,16, 1.01,1.021, order = 0)
ct.controller.trafo.DiscreteTapControl.DiscreteTapControl(net,17, 1.01,1.021, order = 0)
ct.controller.trafo.DiscreteTapControl.DiscreteTapControl(net,18, 1.01,1.021, order = 0)



"""

Launch the Power Flow routine here 

+

Display the results you need

"""

# Run power flow
pp.runpp(net, algorithm='nr', calculate_voltage_angles=True)

# Display results
print("\n=== Power Flow Results ===")
print(f"\nConverged: {net.converged}")
if net.converged:
    print("\nBus Voltages (pu):")
    print(net.res_bus[['vm_pu', 'va_degree']])
    print("\nLine Loading (%):")
    line_results = net.res_line[['loading_percent', 'p_from_mw', 'q_from_mvar']].copy()
    line_results.insert(0, 'name', net.line['name'].values)
    line_results.insert(1, 'from_bus', net.line['from_bus'].map(net.bus['name']).values)
    line_results.insert(2, 'to_bus', net.line['to_bus'].map(net.bus['name']).values)
    print(line_results)
    print("\nGenerator Results:")
    print(net.res_gen[['p_mw', 'q_mvar', 'vm_pu']])
else:
    print("Power flow did not converge!")

line_idx = net.line[(net.line['from_bus'] == N5) & (net.line['to_bus'] == N4)].index[0]
from_bus = net.line.at[line_idx, 'from_bus']
to_bus = net.line.at[line_idx, 'to_bus']

# Tensions et angles (résultats du load flow)
V_from_pu = net.res_bus.at[from_bus, 'vm_pu']  # en p.u.
V_to_pu = net.res_bus.at[to_bus, 'vm_pu']
theta_from = np.deg2rad(net.res_bus.at[from_bus, 'va_degree'])
theta_to = np.deg2rad(net.res_bus.at[to_bus, 'va_degree'])

vn_kv = net.bus.at[from_bus, 'vn_kv']
length = net.line.at[line_idx, 'length_km']
r_ohm_per_km = net.line.at[line_idx, 'r_ohm_per_km']
x_ohm_per_km = net.line.at[line_idx, 'x_ohm_per_km']
c_nf_per_km = net.line.at[line_idx, 'c_nf_per_km']

# Impédance série totale de la ligne (en Ohms)
omega = 2 * np.pi * 50.0
r = r_ohm_per_km * length
x = x_ohm_per_km * length
Z_ohm = r + 1j * x

C_total = c_nf_per_km * 1e-9 * length  # Capacité totale en Farads
Ysh_siemens = 1j * omega * C_total 

# Base du système
Sbase_MVA = net.sn_mva  
Vbase_kV = vn_kv  # 380 kV (tension ligne-ligne)
Zbase = (Vbase_kV**2) / Sbase_MVA
Ybase = 1 / Zbase  

# Conversion des impédances en p.u.
Z_pu = Z_ohm / Zbase
Ysh_pu = Ysh_siemens / Ybase

# Tensions en p.u.
Vf_pu = V_from_pu * np.exp(1j * theta_from) # il faut passer l'angle pcq la tension reelle seul ne suffit pas 
Vt_pu = V_to_pu * np.exp(1j * theta_to)

# Courant série en p.u.
I_series_pu = (Vf_pu - Vt_pu) / Z_pu

# Courant shunt côté 'from' en p.u.
I_sh_from_pu = 0.5 * Ysh_pu * Vf_pu

# Courant total côté'from' en p.u.
I_from_pu = I_series_pu + I_sh_from_pu

# Puissance complexe côté 'from' en p.u.
S_from_pu = Vf_pu * np.conj(I_from_pu)

# Conversion en MW et MVAr
P_from_calc = S_from_pu.real * Sbase_MVA  # MW
Q_from_calc = S_from_pu.imag * Sbase_MVA  # MVAr

# Comparaison avec pandapower
P_from_pp = net.res_line.at[line_idx, 'p_from_mw']
Q_from_pp = net.res_line.at[line_idx, 'q_from_mvar']

print(f"\n=== Ligne {net.line.at[line_idx, 'name']} ===")
print(f"\n--- Paramètres de base ---")
print(f"Sbase: {Sbase_MVA} MVA")
print(f"Vbase: {Vbase_kV} kV (ligne-ligne)")
print(f"Zbase: {Zbase:.3f} ohm")
print(f"Ybase: {Ybase:.6f} S")

print(f"\n--- Impédances de ligne ---")
print(f"Z (Ohms):  {abs(Z_ohm):.3f} ∠ {np.rad2deg(np.angle(Z_ohm)):.3f}°")
print(f"Z (p.u.):  {abs(Z_pu):.6f} ∠ {np.rad2deg(np.angle(Z_pu)):.3f}°")
print(f"Ysh (Siemens): {abs(Ysh_siemens):.6e} ∠ {np.rad2deg(np.angle(Ysh_siemens)):.3f}°")
print(f"Ysh (p.u.):    {abs(Ysh_pu):.6f} ∠ {np.rad2deg(np.angle(Ysh_pu)):.3f}°")

print(f"\n--- Tensions ---")
print(f"V_from: {V_from_pu:.5f} ∠ {np.rad2deg(theta_from):.3f}° p.u.")
print(f"V_to:   {V_to_pu:.5f} ∠ {np.rad2deg(theta_to):.3f}° p.u.")

print(f"\n--- Courants en p.u. ---")
print(f"I_series: {abs(I_series_pu):.5f} ∠ {np.rad2deg(np.angle(I_series_pu)):.3f}° p.u.")
print(f"I_shunt:  {abs(I_sh_from_pu):.5f} ∠ {np.rad2deg(np.angle(I_sh_from_pu)):.3f}° p.u.")
print(f"I_total:  {abs(I_from_pu):.5f} ∠ {np.rad2deg(np.angle(I_from_pu)):.3f}° p.u.")

print(f"\n--- Puissances")
print(f"P_from (calcul manuel): {P_from_calc:.3f} MW")
print(f"P_from (pandapower):    {P_from_pp:.3f} MW")
print(f"Erreur P: {abs(P_from_calc - P_from_pp):.3f} MW ({abs(P_from_calc - P_from_pp)/abs(P_from_pp)*100:.2f}%)")

print(f"\nQ_from (calcul manuel): {Q_from_calc:.3f} MVAr")
print(f"Q_from (pandapower):    {Q_from_pp:.3f} MVAr")
print(f"Erreur Q: {abs(Q_from_calc - Q_from_pp):.3f} MVAr ({abs(Q_from_calc - Q_from_pp)/abs(Q_from_pp)*100:.2f}%)")

# Vérification du courant en kA
Ibase = (Sbase_MVA * 1000) / (np.sqrt(3) * Vbase_kV)  # Courant de base en A
I_from_ka_calc = abs(I_from_pu) * Ibase / 1000  # en kA
I_from_ka_pp = net.res_line.at[line_idx, 'i_from_ka']

print(f"\n--- Vérification du courant ---")
print(f"Ibase: {Ibase:.3f} A")
print(f"I_from (calcul): {I_from_ka_calc:.4f} kA")
print(f"I_from (pandapower): {I_from_ka_pp:.4f} kA")
print(f"Erreur I: {abs(I_from_ka_calc - I_from_ka_pp):.6f} kA")

# ============================
#        Q1.2 : Bilan
# ============================

# Courant série côté "to" (p.u.)
I_series_to_pu = (Vt_pu - Vf_pu) / Z_pu

# Courant shunt côté "to" (p.u.)
I_sh_to_pu = 0.5 * Ysh_pu * Vt_pu

# Courant total côté "to"
I_to_pu = I_series_to_pu + I_sh_to_pu

# Puissance complexe côté "to" (p.u.)
S_to_pu = Vt_pu * np.conj(I_to_pu)

# Conversion en MW et MVAr
P_to_calc = S_to_pu.real * Sbase_MVA
Q_to_calc = S_to_pu.imag * Sbase_MVA

# Pertes
P_loss_calc = P_from_calc + P_to_calc
Q_loss_calc = Q_from_calc + Q_to_calc

# Comparaison avec pandapower
P_to_pp = net.res_line.at[line_idx, 'p_to_mw']
Q_to_pp = net.res_line.at[line_idx, 'q_to_mvar']
P_loss_pp = net.res_line.at[line_idx, 'pl_mw']     # pertes actives pandapower

print("\n=== Q1.2 : Bilan de puissance ===")
print(f"P_to (calcul): {P_to_calc:.4f} MW")
print(f"P_to (pandapower): {P_to_pp:.4f} MW\n")

print(f"Q_to (calcul): {Q_to_calc:.4f} MVAr")
print(f"Q_to (pandapower): {Q_to_pp:.4f} MVAr\n")

print(f"Pertes P (calcul): {P_loss_calc:.6f} MW")
print(f"Pertes P (pandapower): {P_loss_pp:.6f} MW\n")

print(f"Pertes Q (calcul): {Q_loss_calc:.6f} MVAr")


# ========================================
# Calcul côté 'from' (déjà fait en Q1.1)
# ========================================

line_idx = net.line[(net.line['from_bus'] == N5) & 
                    (net.line['to_bus'] == N4)].index[0]

from_bus = net.line.at[line_idx, 'from_bus']
to_bus = net.line.at[line_idx, 'to_bus']

# Tensions complexes
V_from_pu = net.res_bus.at[from_bus, 'vm_pu']
V_to_pu = net.res_bus.at[to_bus, 'vm_pu']
theta_from = np.deg2rad(net.res_bus.at[from_bus, 'va_degree'])
theta_to = np.deg2rad(net.res_bus.at[to_bus, 'va_degree'])

# Paramètres de ligne
vn_kv = net.bus.at[from_bus, 'vn_kv']
length = net.line.at[line_idx, 'length_km']
r = net.line.at[line_idx, 'r_ohm_per_km'] * length
x = net.line.at[line_idx, 'x_ohm_per_km'] * length
c = net.line.at[line_idx, 'c_nf_per_km'] * length

# Bases
Sbase_MVA = net.sn_mva
Vbase_kV = vn_kv
Zbase = Vbase_kV**2 / Sbase_MVA
Ybase = 1 / Zbase

# Conversion en p.u.
Z_pu = (r + 1j * x) / Zbase
omega = 2 * np.pi * 50
Ysh_pu = (1j * omega * c * 1e-9) / Ybase

# Phaseurs
Vf_pu = V_from_pu * np.exp(1j * theta_from)
Vt_pu = V_to_pu * np.exp(1j * theta_to)

# Courants côté 'from'
I_series_pu = (Vf_pu - Vt_pu) / Z_pu
I_sh_from_pu = 0.5 * Ysh_pu * Vf_pu
I_from_pu = I_series_pu + I_sh_from_pu

# Puissance côté 'from'
S_from_pu = Vf_pu * np.conj(I_from_pu)
P_from_calc = S_from_pu.real * Sbase_MVA
Q_from_calc = S_from_pu.imag * Sbase_MVA

# ========================================
# Calcul côté 'to'
# ========================================

I_series_pu_to = I_series_pu  # Même courant physique

# Courant shunt côté 'to'
I_sh_to_pu = 0.5 * Ysh_pu * Vt_pu

# Courant total côté 'to'
I_to_pu = I_series_pu - I_sh_to_pu  # Le shunt est en parallèle, donc soustrait

# Puissance côté 'to'
# Convention: puissance ENTRANT dans le bus 'to' (sortant de la ligne)
S_to_pu = Vt_pu * np.conj(I_to_pu)
P_to_calc = -S_to_pu.real * Sbase_MVA  # Négatif car convention inverse
Q_to_calc = -S_to_pu.imag * Sbase_MVA

# ========================================
# Bilan de puissance (PERTES)
# ========================================

# Pertes actives
Delta_P_calc = P_from_calc + P_to_calc  

# Pertes/Génération réactives
Delta_Q_calc = Q_from_calc + Q_to_calc 

# ========================================
# Comparaison avec pandapower
# ========================================

P_from_pp = net.res_line.at[line_idx, 'p_from_mw']
Q_from_pp = net.res_line.at[line_idx, 'q_from_mvar']
P_to_pp = net.res_line.at[line_idx, 'p_to_mw']
Q_to_pp = net.res_line.at[line_idx, 'q_to_mvar']

Delta_P_pp = P_from_pp + P_to_pp
Delta_Q_pp = Q_from_pp + Q_to_pp

# ========================================
# Affichage des résultats
# ========================================

print(f"\n{'='*60}")
print(f"Q1.2 : BILAN DE PUISSANCE LIGNE 5-N4")
print(f"{'='*60}")

print(f"\n--- Puissances côté 'from' (N5) ---")
print(f"P_from (calcul):     {P_from_calc:>10.4f} MW")
print(f"P_from (pandapower): {P_from_pp:>10.4f} MW")
print(f"Q_from (calcul):     {Q_from_calc:>10.4f} MVAr")
print(f"Q_from (pandapower): {Q_from_pp:>10.4f} MVAr")

print(f"\n--- Puissances côté 'to' (N4) ---")
print(f"P_to (calcul):       {P_to_calc:>10.4f} MW")
print(f"P_to (pandapower):   {P_to_pp:>10.4f} MW")
print(f"Q_to (calcul):       {Q_to_calc:>10.4f} MVAr")
print(f"Q_to (pandapower):   {Q_to_pp:>10.4f} MVAr")

print(f"\n--- Bilan (Pertes) ---")
print(f"ΔP (calcul):         {Delta_P_calc:>10.4f} MW")
print(f"ΔP (pandapower):     {Delta_P_pp:>10.4f} MW")
print(f"Erreur:              {abs(Delta_P_calc - Delta_P_pp):>10.4f} MW")

print(f"\nΔQ (calcul):         {Delta_Q_calc:>10.4f} MVAr")
print(f"ΔQ (pandapower):     {Delta_Q_pp:>10.4f} MVAr")
print(f"Erreur:              {abs(Delta_Q_calc - Delta_Q_pp):>10.4f} MVAr")

print(f"\n--- Interprétation ---")
if Delta_P_calc > 0:
    print(f" Pertes actives: {Delta_P_calc:.4f} MW (effet Joule)")
else:
    print(f" Gain actif impossible: {Delta_P_calc:.4f} MW")

if Delta_Q_calc > 0:
    print(f" Génération réactive nette: {Delta_Q_calc:.4f} MVAr (effet capacitif)")
elif Delta_Q_calc < 0:
    print(f" Consommation réactive nette: {abs(Delta_Q_calc):.4f} MVAr (effet inductif)")
else:
    print(f" Pas de pertes/génération réactive nette")

print(f"\n--- Vérification physique ---")
# Les pertes Joule théoriques
I_rms_pu = abs(I_series_pu)
R_pu = Z_pu.real
P_joule_calc = I_rms_pu**2 * R_pu * Sbase_MVA
print(f"Pertes Joule théoriques (I²R): {P_joule_calc:.4f} MW")
print(f"Cohérence: {abs(P_joule_calc - Delta_P_calc) < 0.01}")

import numpy as np

# ========================================
# DONNÉES DE LA LIGNE
# ========================================

line_idx = net.line[(net.line['from_bus'] == N5) & 
                    (net.line['to_bus'] == N4)].index[0]

# Paramètres par km
r_per_km = net.line.at[line_idx, 'r_ohm_per_km']  
x_per_km = net.line.at[line_idx, 'x_ohm_per_km']  
c_per_km = net.line.at[line_idx, 'c_nf_per_km']   
length_km = net.line.at[line_idx, 'length_km']    

# Tension nominale (ligne-ligne)
Vn_kV = net.bus.at[net.line.at[line_idx, 'from_bus'], 'vn_kv']  # 380 kV

# Fréquence
f = net.f_hz  # 50 Hz
omega = 2 * np.pi * f

print(f"\n{'='*60}")
print(f"Q1.3 : SURGE IMPEDANCE LOADING (SIL)")
print(f"{'='*60}")

# ========================================
# CALCUL DE L'IMPÉDANCE CARACTÉRISTIQUE Zc
# ========================================

# Impédance série par km (complexe)
z_per_km = r_per_km + 1j * x_per_km 

# Admittance shunt par km (complexe)
# y_per_km = G + j*ω*C, avec G ≈ 0 (pas de conductance)
C_per_km_F = c_per_km * 1e-9 
y_per_km = 1j * omega * C_per_km_F  # S/km

# Impédance caractéristique (complex)
Zc = np.sqrt(z_per_km / y_per_km)

print(f"\n--- Paramètres de ligne (par km) ---")
print(f"z (série):   {abs(z_per_km):.3f} ∠ {np.angle(z_per_km, deg=True):.2f}° ohm/km")
print(f"y (shunt):   {abs(y_per_km):.6e} ∠ {np.angle(y_per_km, deg=True):.2f}° S/km")
print(f"\n--- Impédance caractéristique ---")
print(f"Zc = {abs(Zc):.2f} ∠ {np.angle(Zc, deg=True):.2f}° Ω")

# ========================================
# CALCUL DU SURGE IMPEDANCE LOADING (SIL)
# ========================================

# Formule du SIL (triphasé, tension ligne-ligne)
SIL_MW = (Vn_kV**2) / abs(Zc)  # MW

print(f"\n--- Surge Impedance Loading (SIL) ---")
print(f"Vn = {Vn_kV} kV (ligne-ligne)")
print(f"SIL = Vn² / |Zc| = {Vn_kV}² / {abs(Zc):.2f}")
print(f"SIL = {SIL_MW:.2f} MW")

# ========================================
# PUISSANCE ACTUELLE DANS LA LIGNE
# ========================================

# Puissance apparente transmise (côté from)
P_from = net.res_line.at[line_idx, 'p_from_mw']
Q_from = net.res_line.at[line_idx, 'q_from_mvar']
S_from = np.sqrt(P_from**2 + Q_from**2)

# Taux de charge par rapport au SIL
loading_SIL = (S_from / SIL_MW) * 100

print(f"\n--- Charge actuelle de la ligne ---")
print(f"P_from = {P_from:.2f} MW")
print(f"Q_from = {Q_from:.2f} MVAr")
print(f"S_from = {S_from:.2f} MVA")
print(f"\nLoading par rapport au SIL : {loading_SIL:.1f}%")

# ========================================
# VÉRIFICATION ALTERNATIVE
# ========================================

# Calcul de Zc à partir de L et C
L_per_km_H = x_per_km / omega  # Inductance par km (H/km)
C_per_km_F = c_per_km * 1e-9   # Capacité par km (F/km)

Zc_alternative = np.sqrt(L_per_km_H / C_per_km_F)

print(f"\n--- Vérification ---")
print(f"L = {L_per_km_H:.6f} H/km")
print(f"C = {C_per_km_F:.9f} F/km")
print(f"Zc ((L/C)^(1/2)) = {Zc_alternative:.2f} ohm")
print(f"Écart avec calcul direct : {abs(abs(Zc) - Zc_alternative):.4f} ohm")

# ========================================
# COMPARAISON MODULE vs MAGNITUDE
# ========================================

print(f"\n--- Analyse de Zc ---")
print(f"|Zc| (magnitude) = {abs(Zc):.2f} Ω")
print(f"Re(Zc) = {Zc.real:.2f} Ω")
print(f"Im(Zc) = {Zc.imag:.2f} Ω")
print(f"φ(Zc) = {np.angle(Zc, deg=True):.2f}°")

if abs(np.angle(Zc, deg=True)) < 5:
    print("→ Zc est quasi-réel (ligne avec faibles pertes)")
else:
    print("→ Zc a une composante imaginaire significative")

import numpy as np

# ========================================
# Q1.4 : COURANT DANS LA LIGNE ET COMPARAISON
# ========================================

line_idx = net.line[(net.line['from_bus'] == N5) & 
                    (net.line['to_bus'] == N4)].index[0]

print(f"\n{'='*60}")
print(f"Q1.4 : COURANT DANS LA LIGNE N5-N4")
print(f"{'='*60}")

# ========================================
# MÉTHODE 1 : Extraction directe depuis pandapower
# ========================================

# Courant calculé par pandapower (côté 'from')
I_from_ka_pp = net.res_line.at[line_idx, 'i_from_ka']

# Courant maximal de la ligne
I_max_ka = net.line.at[line_idx, 'max_i_ka']

# Taux de charge (loading)
loading_percent_pp = net.res_line.at[line_idx, 'loading_percent']

print(f"\n--- Résultats pandapower ---")
print(f"I_from = {I_from_ka_pp:.4f} kA")
print(f"I_max  = {I_max_ka:.4f} kA")
print(f"Loading = {loading_percent_pp:.2f}%")

# ========================================
# MÉTHODE 2 : Calcul manuel du courant
# ========================================

from_bus = net.line.at[line_idx, 'from_bus']
to_bus = net.line.at[line_idx, 'to_bus']

# Tensions
V_from_pu = net.res_bus.at[from_bus, 'vm_pu']
V_to_pu = net.res_bus.at[to_bus, 'vm_pu']
theta_from = np.deg2rad(net.res_bus.at[from_bus, 'va_degree'])
theta_to = np.deg2rad(net.res_bus.at[to_bus, 'va_degree'])

# Paramètres de ligne
vn_kv = net.bus.at[from_bus, 'vn_kv']
length = net.line.at[line_idx, 'length_km']
r = net.line.at[line_idx, 'r_ohm_per_km'] * length
x = net.line.at[line_idx, 'x_ohm_per_km'] * length
c = net.line.at[line_idx, 'c_nf_per_km'] * length

# Bases
Sbase_MVA = net.sn_mva
Zbase = vn_kv**2 / Sbase_MVA
Ybase = 1 / Zbase

# Conversion en p.u.
Z_pu = (r + 1j * x) / Zbase
omega = 2 * np.pi * 50
Ysh_pu = (1j * omega * c * 1e-9) / Ybase

# Phaseurs
Vf_pu = V_from_pu * np.exp(1j * theta_from)
Vt_pu = V_to_pu * np.exp(1j * theta_to)

# Courants en p.u.
I_series_pu = (Vf_pu - Vt_pu) / Z_pu
I_sh_from_pu = 0.5 * Ysh_pu * Vf_pu
I_from_pu = I_series_pu + I_sh_from_pu

# Courant de base
I_base = (Sbase_MVA * 1000) / (np.sqrt(3) * vn_kv)  # en A

# Conversion en kA
I_from_ka_calc = abs(I_from_pu) * I_base / 1000

print(f"\n--- Calcul manuel ---")
print(f"I_base = {I_base:.2f} A")
print(f"I_from (p.u.) = {abs(I_from_pu):.5f} ∠ {np.angle(I_from_pu, deg=True):.2f}°")
print(f"I_from (calcul) = {I_from_ka_calc:.4f} kA")
print(f"Erreur avec pandapower = {abs(I_from_ka_calc - I_from_ka_pp):.6f} kA")

# ========================================
# MÉTHODE 3 : Calcul direct à partir de S et V
# ========================================

# Puissance apparente côté 'from'
P_from = net.res_line.at[line_idx, 'p_from_mw']
Q_from = net.res_line.at[line_idx, 'q_from_mvar']
S_from = np.sqrt(P_from**2 + Q_from**2)

# Tension ligne-ligne au bus 'from' (en kV)
V_from_kV = V_from_pu * vn_kv

# Courant triphasé
I_from_ka_S = S_from / (np.sqrt(3) * V_from_kV)

print(f"\n--- Vérification via S et V ---")
print(f"S_from = {S_from:.2f} MVA")
print(f"V_from = {V_from_kV:.2f} kV (ligne-ligne)")
print(f"I_from = S/(√3·V) = {S_from:.2f}/(√3·{V_from_kV:.2f}) = {I_from_ka_S:.4f} kA")

# ========================================
# COMPARAISON AU COURANT NOMINAL
# ========================================

# Taux de charge manuel
loading_percent_calc = (I_from_ka_calc / I_max_ka) * 100

print(f"\n--- Comparaison au courant nominal ---")
print(f"I_from / I_max = {I_from_ka_calc:.4f} / {I_max_ka:.4f} = {loading_percent_calc:.2f}%")

if loading_percent_calc < 100:
    print(f"La ligne est exploitée en sécurité ({loading_percent_calc:.1f}% de charge)")
elif loading_percent_calc < 110:
    print(f"La ligne est proche de sa limite ({loading_percent_calc:.1f}% de charge)")
else:
    print(f"SURCHARGE ! La ligne dépasse sa capacité ({loading_percent_calc:.1f}% de charge)")

# ========================================
# CALCUL DU COURANT NOMINAL THÉORIQUE
# ========================================

# Le courant max peut être vérifié avec la puissance nominale
# Pour une ligne, I_max dépend de la limite thermique
# Souvent, max_i_ka est fixé directement ou calculé via des normes

print(f"\n--- Informations complémentaires ---")
print(f"Puissance nominale (si basée sur I_max) :")
S_nominal_MVA = np.sqrt(3) * vn_kv * I_max_ka
print(f"S_nominal = 3^(1/2) · V_n · I_max = √3 · {vn_kv} · {I_max_ka:.4f}")
print(f"S_nominal = {S_nominal_MVA:.2f} MVA")

# Facteur de puissance actuel
pf_from = P_from / S_from
print(f"\nFacteur de puissance actuel : {pf_from:.4f}")
print(f"Angle φ = {np.rad2deg(np.arccos(pf_from)):.2f}°")

# ========================================
# TABLEAU RÉCAPITULATIF
# ========================================

print(f"\n{'='*60}")
print(f"RÉCAPITULATIF")
print(f"{'='*60}")
print(f"{'Grandeur':<30} {'Valeur':>15} {'Unité':>10}")
print(f"{'-'*60}")
print(f"{'Courant from (pandapower)':<30} {I_from_ka_pp:>15.4f} {'kA':>10}")
print(f"{'Courant from (calcul p.u.)':<30} {I_from_ka_calc:>15.4f} {'kA':>10}")
print(f"{'Courant from (via S/V)':<30} {I_from_ka_S:>15.4f} {'kA':>10}")
print(f"{'Courant maximal':<30} {I_max_ka:>15.4f} {'kA':>10}")
print(f"{'Taux de charge':<30} {loading_percent_calc:>15.2f} {'%':>10}")
print(f"{'Puissance apparente':<30} {S_from:>15.2f} {'MVA':>10}")
print(f"{'Puissance nominale (théorique)':<30} {S_nominal_MVA:>15.2f} {'MVA':>10}")
print(f"{'='*60}")

# trouver l'indice du transfo Nc-Nd
trafo_idx = 0  # adapter
P_from_trafo_MW = net.res_trafo.at[trafo_idx, 'p_hv_mw']  # HV side
Q_from_trafo_MVAr = net.res_trafo.at[trafo_idx, 'q_hv_mvar']
P_to_trafo_MW = net.res_trafo.at[trafo_idx, 'p_lv_mw']
Q_to_trafo_MVAr = net.res_trafo.at[trafo_idx, 'q_lv_mvar']
print(P_from_trafo_MW, Q_from_trafo_MVAr, P_to_trafo_MW, Q_to_trafo_MVAr)
# pertes
P_loss_trafo = P_from_trafo_MW - P_to_trafo_MW
Q_loss_trafo = Q_from_trafo_MVAr - Q_to_trafo_MVAr
print("Trafo losses (MW,MVAr):", P_loss_trafo, Q_loss_trafo)

import numpy as np

# ========================================
# Q1.5 : TRANSITS DE PUISSANCE TRANSFORMATEUR N5-N106
# ========================================

# Identification du transformateur N5-N106
trafo_idx = net.trafo[net.trafo['name'] == 'N5N106'].index[0]

print(f"\n{'='*60}")
print(f"Q1.5 : TRANSITS DE PUISSANCE TRANSFORMATEUR N5-N106")
print(f"{'='*60}")

# ========================================
# EXTRACTION DES DONNÉES PANDAPOWER
# ========================================

# Bus HV et LV
hv_bus = net.trafo.at[trafo_idx, 'hv_bus']
lv_bus = net.trafo.at[trafo_idx, 'lv_bus']

hv_bus_name = net.bus.at[hv_bus, 'name']
lv_bus_name = net.bus.at[lv_bus, 'name']

# Puissances côté HV (High Voltage)
P_hv_pp = net.res_trafo.at[trafo_idx, 'p_hv_mw']
Q_hv_pp = net.res_trafo.at[trafo_idx, 'q_hv_mvar']

# Puissances côté LV (Low Voltage)
P_lv_pp = net.res_trafo.at[trafo_idx, 'p_lv_mw']
Q_lv_pp = net.res_trafo.at[trafo_idx, 'q_lv_mvar']

print(f"\n--- Informations du transformateur ---")
print(f"Nom : {net.trafo.at[trafo_idx, 'name']}")
print(f"Bus HV : {hv_bus_name} ({net.trafo.at[trafo_idx, 'vn_hv_kv']} kV)")
print(f"Bus LV : {lv_bus_name} ({net.trafo.at[trafo_idx, 'vn_lv_kv']} kV)")
print(f"Sn : {net.trafo.at[trafo_idx, 'sn_mva']} MVA")

print(f"\n--- Puissances côté HV (pandapower) ---")
print(f"P_HV = {P_hv_pp:.4f} MW")
print(f"Q_HV = {Q_hv_pp:.4f} MVAr")

print(f"\n--- Puissances côté LV (pandapower) ---")
print(f"P_LV = {P_lv_pp:.4f} MW")
print(f"Q_LV = {Q_lv_pp:.4f} MVAr")

# ========================================
# CALCUL MANUEL DES TRANSITS (CÔTÉ HV)
# ========================================

# Tensions aux bus (résultats du load flow)
V_hv_pu = net.res_bus.at[hv_bus, 'vm_pu']
V_lv_pu = net.res_bus.at[lv_bus, 'vm_pu']
theta_hv = np.deg2rad(net.res_bus.at[hv_bus, 'va_degree'])
theta_lv = np.deg2rad(net.res_bus.at[lv_bus, 'va_degree'])

# Paramètres du transformateur
Sn_trafo = net.trafo.at[trafo_idx, 'sn_mva']
vn_hv_kv = net.trafo.at[trafo_idx, 'vn_hv_kv']
vn_lv_kv = net.trafo.at[trafo_idx, 'vn_lv_kv']
vk_percent = net.trafo.at[trafo_idx, 'vk_percent']
vkr_percent = net.trafo.at[trafo_idx, 'vkr_percent']
pfe_kw = net.trafo.at[trafo_idx, 'pfe_kw']
i0_percent = net.trafo.at[trafo_idx, 'i0_percent']

# Impédance du transformateur (en p.u. sur sa base propre)
Zk_pu_own = vk_percent / 100
Rk_pu_own = vkr_percent / 100
Xk_pu_own = np.sqrt(Zk_pu_own**2 - Rk_pu_own**2)

# Conversion à la base commune (100 MVA)
Sbase_MVA = net.sn_mva
Zk_pu = Zk_pu_own * (Sbase_MVA / Sn_trafo)
Rk_pu = Rk_pu_own * (Sbase_MVA / Sn_trafo)
Xk_pu = Xk_pu_own * (Sbase_MVA / Sn_trafo)

Z_trafo_pu = Rk_pu + 1j * Xk_pu

# Rapport de transformation (avec tap)
tap_pos = net.trafo.at[trafo_idx, 'tap_pos']
tap_neutral = net.trafo.at[trafo_idx, 'tap_neutral']
tap_step_percent = net.trafo.at[trafo_idx, 'tap_step_percent']
tap_side = net.trafo.at[trafo_idx, 'tap_side']

# Calcul du rapport effectif
tap_correction = 1 + (tap_pos - tap_neutral) * tap_step_percent / 100

if tap_side == "hv":
    n_ratio = (vn_hv_kv / vn_lv_kv) * tap_correction
else:  # tap_side == "lv"
    n_ratio = (vn_hv_kv / vn_lv_kv) / tap_correction

print(f"\n--- Paramètres du transformateur ---")
print(f"Zk (base propre) = {Zk_pu_own:.6f} p.u. (sur {Sn_trafo} MVA)")
print(f"Zk (base 100 MVA) = {abs(Z_trafo_pu):.6f} ∠ {np.angle(Z_trafo_pu, deg=True):.2f}° p.u.")
print(f"Tap position = {tap_pos} (neutral = {tap_neutral})")
print(f"Rapport n = {n_ratio:.6f}")

# Phaseurs de tension (en p.u. sur base commune)
V_hv_complex = V_hv_pu * np.exp(1j * theta_hv)
V_lv_complex = V_lv_pu * np.exp(1j * theta_lv)

# Tension LV ramenée au primaire
V_lv_referred = V_lv_complex * n_ratio

# Courant dans le transformateur (approximation sans magnétisation)
I_trafo_pu = (V_hv_complex - V_lv_referred) / Z_trafo_pu

# Puissance complexe côté HV
S_hv_pu = V_hv_complex * np.conj(I_trafo_pu)
P_hv_calc = S_hv_pu.real * Sbase_MVA
Q_hv_calc = S_hv_pu.imag * Sbase_MVA

print(f"\n--- Calcul manuel (côté HV) ---")
print(f"V_HV = {V_hv_pu:.5f} ∠ {np.rad2deg(theta_hv):.3f}° p.u.")
print(f"V_LV = {V_lv_pu:.5f} ∠ {np.rad2deg(theta_lv):.3f}° p.u.")
print(f"V_LV (ramené au HV) = {abs(V_lv_referred):.5f} ∠ {np.angle(V_lv_referred, deg=True):.3f}° p.u.")
print(f"I_trafo = {abs(I_trafo_pu):.5f} ∠ {np.angle(I_trafo_pu, deg=True):.3f}° p.u.")

print(f"\nP_HV (calcul) = {P_hv_calc:.4f} MW")
print(f"P_HV (pandapower) = {P_hv_pp:.4f} MW")
print(f"Erreur P = {abs(P_hv_calc - P_hv_pp):.4f} MW")

print(f"\nQ_HV (calcul) = {Q_hv_calc:.4f} MVAr")
print(f"Q_HV (pandapower) = {Q_hv_pp:.4f} MVAr")
print(f"Erreur Q = {abs(Q_hv_calc - Q_hv_pp):.4f} MVAr")

# ========================================
# VÉRIFICATION VIA COURANT
# ========================================

# Courant côté HV en kA
I_base_hv = (Sbase_MVA * 1000) / (np.sqrt(3) * vn_hv_kv)
I_hv_ka_calc = abs(I_trafo_pu) * I_base_hv / 1000
I_hv_ka_pp = net.res_trafo.at[trafo_idx, 'i_hv_ka']

print(f"\n--- Vérification du courant HV ---")
print(f"I_HV (calcul) = {I_hv_ka_calc:.4f} kA")
print(f"I_HV (pandapower) = {I_hv_ka_pp:.4f} kA")
print(f"Erreur I = {abs(I_hv_ka_calc - I_hv_ka_pp):.6f} kA")

# ========================================
# RÉCAPITULATIF
# ========================================

print(f"\n{'='*60}")
print(f"RÉCAPITULATIF Q1.5")
print(f"{'='*60}")
print(f"Transformateur : N5-N106 ({vn_hv_kv} kV / {vn_lv_kv} kV, {Sn_trafo} MVA)")
print(f"\nPuissances côté HV (High Voltage) :")
print(f"  P_HV = {P_hv_pp:.4f} MW")
print(f"  Q_HV = {Q_hv_pp:.4f} MVAr")
print(f"  S_HV = {np.sqrt(P_hv_pp**2 + Q_hv_pp**2):.4f} MVA")
print(f"\nCourant côté HV :")
print(f"  I_HV = {I_hv_ka_pp:.4f} kA")
print(f"{'='*60}")