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

line_idx = net.line[(net.line['from_bus'] == N5) & (net.line['to_bus'] == N4)].index[1]

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

# Bases
Sbase_MVA = net.sn_mva  
Vbase_kV = vn_kv  # 380 kV (tension ligne-ligne)
Zbase = (Vbase_kV**2) / Sbase_MVA
Ybase = 1 / Zbase  
Ibase = Sbase_MVA / (np.sqrt(3) * Vbase_kV)

# ohm et siemens vers p.u.
Z_pu = Z_ohm / Zbase
Ysh_pu = Ysh_siemens / Ybase

# Tensions et courant en p.u.
Vf_pu = V_from_pu * np.exp(1j * theta_from) # il faut passer l'angle pcq la tension reelle seul ne suffit pas 
Vt_pu = V_to_pu * np.exp(1j * theta_to)
I_series_pu = (Vf_pu - Vt_pu) / Z_pu
I_sh_from_pu = 0.5 * Ysh_pu * Vf_pu
I_from_pu = I_series_pu + I_sh_from_pu

# Puissance complexe côté 'from' en p.u.
S_from_pu = Vf_pu * np.conj(I_from_pu)

# puissances en MW et MVAr
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

# Vérification du courant
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

# Courant Ito
I_series_to_pu = (Vt_pu - Vf_pu) / Z_pu
I_sh_to_pu = 0.5 * Ysh_pu * Vt_pu
I_to_pu = I_series_to_pu + I_sh_to_pu

# Puissance complexe cote to (p.u.)
S_to_pu = Vt_pu * np.conj(I_to_pu)

# Conversion en MW et MVAr
P_to_calc = S_to_pu.real * Sbase_MVA
Q_to_calc = S_to_pu.imag * Sbase_MVA


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

Delta_P_pp = net.res_line.at[line_idx, 'pl_mw']
Delta_Q_pp = net.res_line.at[line_idx, 'ql_mvar']

# ========================================
# Affichage des résultats
# ========================================

print(f"\n{'='*60}")
print(f"Q1.2 : BILAN DE PUISSANCE LIGNE N5-N4")
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
print(f"dP (calcul):         {Delta_P_calc:>10.4f} MW")
print(f"dP (pandapower):     {Delta_P_pp:>10.4f} MW")
print(f"Erreur:              {abs(Delta_P_calc - Delta_P_pp):>10.4f} MW")

print(f"\ndQ (calcul):         {Delta_Q_calc:>10.4f} MVAr")
print(f"dQ (pandapower):     {Delta_Q_pp:>10.4f} MVAr")
print(f"Erreur:              {abs(Delta_Q_calc - Delta_Q_pp):>10.4f} MVAr")

print(f"\n--- Interprétation ---")
if Delta_P_calc > 0:
    print(f"-> Pertes actives: {Delta_P_calc:.4f} MW (effet Joule)")
else:
    print(f"-> Gain actif impossible: {Delta_P_calc:.4f} MW")

if Delta_Q_calc > 0:
    print(f"Génération réactive nette: {Delta_Q_calc:.4f} MVAr (effet capacitif)")
elif Delta_Q_calc < 0:
    print(f"Consommation réactive nette: {abs(Delta_Q_calc):.4f} MVAr (effet inductif)")
else:
    print(f"Pas de pertes/génération réactive nette")

print(f"\n--- Vérification physique ---")
# Les pertes Joule théoriques
I_rms_pu = abs(I_series_pu)
R_pu = Z_pu.real
P_joule_calc = I_rms_pu**2 * R_pu * Sbase_MVA
print(f"Pertes Joule théoriques (I²R): {P_joule_calc:.4f} MW")
print(f"Cohérence: {abs(P_joule_calc - Delta_P_calc) < 0.01}")

# ========================================
#   Q1.3 : SURGE IMPEDANCE LOADING (SIL)
# ========================================
print(f"\n{'='*60}") 
print(f"Q1.3 : SURGE IMPEDANCE LOADING (SIL)")
print(f"{'='*60}")

# Tension nominale (ligne-ligne)
Vn_kV = net.bus.at[net.line.at[line_idx, 'from_bus'], 'vn_kv']  # 380 kV

# ========================================
# CALCUL DE L'IMPÉDANCE CARACTÉRISTIQUE Zc
# ========================================

# Impédance série par km (complexe)
z_per_km = r_ohm_per_km + 1j * x_ohm_per_km  # ohm/km

# Admittance shunt par km (complexe)
# y_per_km = G + j*ω*C, avec G ≈ 0 (pas de conductance)
C_per_km_F = c_nf_per_km * 1e-9 
y_per_km = 1j * omega * C_per_km_F  # S/km

# Impédance caractéristique (complex)
Zc = np.sqrt(z_per_km / y_per_km)  # ohm

print(f"\n--- Paramètres de ligne (par km) ---")
print(f"z (série):   {abs(z_per_km):.3f} ∠ {np.angle(z_per_km, deg=True):.2f}° Ω/km")
print(f"y (shunt):   {abs(y_per_km):.6e} ∠ {np.angle(y_per_km, deg=True):.2f}° S/km")
print(f"\n--- Impédance caractéristique ---")
print(f"Zc = {abs(Zc):.2f} ∠ {np.angle(Zc, deg=True):.2f}° Ω")
# Tension de phase (pour ligne triphasée)
#V_phase_kV = Vn_kV / np.sqrt(3)  # kV
V_phase_V = Vn_kV* 1e3      # V

# SIL complexe (puissance triphasée)
SIL_complex = (V_phase_V**2) / Zc  # VA

# Conversion en MVA
SIL_MVA = abs(SIL_complex) / 1e6
SIL_angle_deg = np.angle(SIL_complex, deg=True)

print(f"\n--- Surge Impedance Loading (SIL) ---")
print(f"SIL = {SIL_MVA:.2f} MVA ∠ {SIL_angle_deg:.2f}°")

# ========================================
# Q1.4 : COURANT DANS LA LIGNE ET COMPARAISON
# ========================================

print(f"\n{'='*60}")
print(f"Q1.4 : COURANT DANS LA LIGNE N1-N4")
print(f"{'='*60}")

# ========================================
# MÉTHODE 1 : Extraction directe depuis pandapower
# ========================================

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
# fais en 1.1

print(f"\n--- Calcul manuel ---")
print(f"I_base = {Ibase:.2f} A")
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
print(f"S_nominal = √3 · V_n · I_max = √3 · {vn_kv} · {I_max_ka:.4f}")
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

trafo_idx = 0 
P_from_trafo_MW = net.res_trafo.at[trafo_idx, 'p_hv_mw']  # HV side
Q_from_trafo_MVAr = net.res_trafo.at[trafo_idx, 'q_hv_mvar']
P_to_trafo_MW = net.res_trafo.at[trafo_idx, 'p_lv_mw']
Q_to_trafo_MVAr = net.res_trafo.at[trafo_idx, 'q_lv_mvar']
print(P_from_trafo_MW, Q_from_trafo_MVAr, P_to_trafo_MW, Q_to_trafo_MVAr)
# pertes
P_loss_trafo = P_from_trafo_MW - P_to_trafo_MW
Q_loss_trafo = Q_from_trafo_MVAr - Q_to_trafo_MVAr
print("Trafo losses (MW,MVAr):", P_loss_trafo, Q_loss_trafo)

# ========================================
# Q1.5 : TRANSITS DE PUISSANCE TRANSFORMATEUR N2-N107
# ========================================

print(f"\n{'='*60}")
print(f"Q1.5 : TRANSITS DE PUISSANCE TRANSFORMATEUR (côté HV)")
print(f"{'='*60}")
trafo_name = 'N2N107'
trafo_idx = net.trafo[net.trafo['name'] == trafo_name].index[0]
hv_bus = net.trafo.at[trafo_idx, 'hv_bus']
lv_bus = net.trafo.at[trafo_idx, 'lv_bus']
hv_bus_name = net.bus.at[hv_bus, 'name']
lv_bus_name = net.bus.at[lv_bus, 'name']
sn_mva = net.trafo.at[trafo_idx, 'sn_mva']
vn_hv_kv = net.trafo.at[trafo_idx, 'vn_hv_kv']
vn_lv_kv = net.trafo.at[trafo_idx, 'vn_lv_kv']

print(f"\nTransformateur: {trafo_name}")
print(f"HV: {hv_bus_name} ({vn_hv_kv} kV)")
print(f"LV: {lv_bus_name} ({vn_lv_kv} kV)")
print(f"Puissance nominale: {sn_mva} MVA")

# ========================================
# Résultats pandapower
# ========================================

P_hv_pp = net.res_trafo.at[trafo_idx, 'p_hv_mw']
Q_hv_pp = net.res_trafo.at[trafo_idx, 'q_hv_mvar']
I_hv_ka_pp = net.res_trafo.at[trafo_idx, 'i_hv_ka']

print(f"\n--- Résultats pandapower (côté HV) ---")
print(f"P_hv = {P_hv_pp:.4f} MW")
print(f"Q_hv = {Q_hv_pp:.4f} MVAr")
print(f"S_hv = {np.sqrt(P_hv_pp**2 + Q_hv_pp**2):.4f} MVA")
print(f"I_hv = {I_hv_ka_pp:.4f} kA")

# ========================================
# CALCUL MANUEL : S_HV = V_HV × I_HV*
# ========================================

# Récupérer la tension au bus HV (résultats du load flow)
V_hv_pu = net.res_bus.at[hv_bus, 'vm_pu']
theta_hv_deg = net.res_bus.at[hv_bus, 'va_degree']
theta_hv_rad = np.deg2rad(theta_hv_deg)

print(f"\n--- Tension au bus HV ---")
print(f"V_hv = {V_hv_pu:.5f} ∠ {theta_hv_deg:.3f}° p.u.")

# Tension en kV (ligne-ligne)
V_hv_kV = V_hv_pu * vn_hv_kv
print(f"V_hv = {V_hv_kV:.3f} kV (ligne-ligne)")

# Tension complexe (en kV)
V_hv_complex = V_hv_kV * np.exp(1j * theta_hv_rad)

# Courant côté HV (de pandapower)
I_hv_ka = I_hv_ka_pp

# Pour calculer S = V × I*, il faut l'angle du courant
# On peut le déduire de P, Q et V
S_hv_pp_MVA = np.sqrt(P_hv_pp**2 + Q_hv_pp**2)
phi_hv = np.arctan2(Q_hv_pp, P_hv_pp)  # angle de la puissance complexe

print(f"\n--- Angle de puissance ---")
print(f"φ_hv = arctan(Q/P) = {np.rad2deg(phi_hv):.3f}°")

# L'angle du courant par rapport à la référence
# S = V × I* donc I* = S / V
# angle(I*) = angle(S) - angle(V)
# angle(I) = angle(V) - angle(S)
theta_I_hv = theta_hv_rad - phi_hv

print(f"theta_I = theta_V - phi = {np.rad2deg(theta_I_hv):.3f}°")

# Courant complexe (en kA)
I_hv_complex = I_hv_ka * np.exp(1j * theta_I_hv)

print(f"\n--- Courant côté HV ---")
print(f"I_hv = {abs(I_hv_complex):.4f} ∠ {np.rad2deg(np.angle(I_hv_complex)):.3f}° kA")

# ========================================
# Calcul de S_HV = V_HV × I_HV*
# ========================================

# S = V × I* (en MVA)
# V est en kV, I est en kA, donc S = sqrt(3) × V × I pour un système triphasé
S_hv_complex = np.sqrt(3) * V_hv_complex * np.conj(I_hv_complex)

P_hv_calc = S_hv_complex.real
Q_hv_calc = S_hv_complex.imag
S_hv_calc = abs(S_hv_complex)

print(f"\n--- Calcul manuel : S_HV = √3 × V_HV × I_HV* ---")
print(f"P_hv (calcul) = {P_hv_calc:.4f} MW")
print(f"Q_hv (calcul) = {Q_hv_calc:.4f} MVAr")
print(f"S_hv (calcul) = {S_hv_calc:.4f} MVA")

# ========================================
# COMPARAISON
# ========================================

print(f"\n{'='*60}")
print(f"COMPARAISON PANDAPOWER vs CALCUL MANUEL")
print(f"{'='*60}")
print(f"{'Grandeur':<20} {'Pandapower':>15} {'Calcul':>15} {'Erreur':>15}")
print(f"{'-'*65}")
print(f"{'P_hv (MW)':<20} {P_hv_pp:>15.4f} {P_hv_calc:>15.4f} {abs(P_hv_pp - P_hv_calc):>15.6f}")
print(f"{'Q_hv (MVAr)':<20} {Q_hv_pp:>15.4f} {Q_hv_calc:>15.4f} {abs(Q_hv_pp - Q_hv_calc):>15.6f}")
print(f"{'S_hv (MVA)':<20} {np.sqrt(P_hv_pp**2 + Q_hv_pp**2):>15.4f} {S_hv_calc:>15.4f} {abs(np.sqrt(P_hv_pp**2 + Q_hv_pp**2) - S_hv_calc):>15.6f}")

# Calcul des erreurs relatives
err_P = abs(P_hv_calc - P_hv_pp) / abs(P_hv_pp) * 100 if P_hv_pp != 0 else 0
err_Q = abs(Q_hv_calc - Q_hv_pp) / abs(Q_hv_pp) * 100 if Q_hv_pp != 0 else 0

print(f"\n--- Erreurs relatives ---")
print(f"Erreur P: {err_P:.3f}%")
print(f"Erreur Q: {err_Q:.3f}%")
print(f"{'='*60}\n")


# ========================================
# Q1.6 : BILAN DE PUISSANCE TRANSFORMATEUR Nc-Nd
# ========================================

print(f"\n{'='*60}")
print(f"Q1.6 : BILAN DE PUISSANCE TRANSFORMATEUR {trafo_name}")
print(f"{'='*60}")

# ========================================
# A. PUISSANCES CÔTÉ SECONDAIRE (LV)
# ========================================

# Résultats pandapower côté LV
P_lv_pp = net.res_trafo.at[trafo_idx, 'p_lv_mw']
Q_lv_pp = net.res_trafo.at[trafo_idx, 'q_lv_mvar']
I_lv_ka_pp = net.res_trafo.at[trafo_idx, 'i_lv_ka']

print(f"\n--- Résultats pandapower (côté LV) ---")
print(f"P_lv = {P_lv_pp:.4f} MW")
print(f"Q_lv = {Q_lv_pp:.4f} MVAr")
print(f"S_lv = {np.sqrt(P_lv_pp**2 + Q_lv_pp**2):.4f} MVA")
print(f"I_lv = {I_lv_ka_pp:.4f} kA")

V_lv_pu = net.res_bus.at[lv_bus, 'vm_pu']
theta_lv_deg = net.res_bus.at[lv_bus, 'va_degree']
theta_lv_rad = np.deg2rad(theta_lv_deg)

print(f"\n--- Tension au bus LV ---")
print(f"V_lv = {V_lv_pu:.5f} ∠ {theta_lv_deg:.3f}° p.u.")

# Tension en kV
V_lv_kV = V_lv_pu * vn_lv_kv
print(f"V_lv = {V_lv_kV:.3f} kV (ligne-ligne)")

# Tension complexe
V_lv_complex = V_lv_kV * np.exp(1j * theta_lv_rad)

# Angle de la puissance côté LV
S_lv_pp_MVA = np.sqrt(P_lv_pp**2 + Q_lv_pp**2)
phi_lv = np.arctan2(Q_lv_pp, P_lv_pp)

# Angle du courant LV
theta_I_lv = theta_lv_rad - phi_lv

# Courant complexe LV
I_lv_complex = I_lv_ka_pp * np.exp(1j * theta_I_lv)

print(f"\n--- Courant côté LV ---")
print(f"I_lv = {abs(I_lv_complex):.4f} ∠ {np.rad2deg(np.angle(I_lv_complex)):.3f}° kA")

S_lv_complex = np.sqrt(3) * V_lv_complex * np.conj(I_lv_complex)

P_lv_calc = S_lv_complex.real
Q_lv_calc = S_lv_complex.imag
S_lv_calc = abs(S_lv_complex)

print(f"P_lv (calcul) = {P_lv_calc:.4f} MW")
print(f"Q_lv (calcul) = {Q_lv_calc:.4f} MVAr")
print(f"S_lv (calcul) = {S_lv_calc:.4f} MVA")

# ========================================
# B. BILAN DE PUISSANCE (PERTES)
# ========================================

print(f"\n{'='*60}")
print(f"BILAN DE PUISSANCE - PERTES")
print(f"{'='*60}")

# Pertes actives : P_loss = P_HV - P_LV
P_loss_pp = net.res_trafo.at[trafo_idx, 'pl_mw']
P_loss_calc = P_hv_calc + P_lv_calc

print(f"\n--- Pertes actives ---")
print(f"P_loss (pandapower) = {P_loss_pp:.4f} MW")
print(f"P_loss (calcul)     = {P_loss_calc:.4f} MW")
print(f"Erreur              = {abs(P_loss_pp - P_loss_calc):.6f} MW")

# Pertes réactives : Q_loss = Q_HV - Q_LV
Q_loss_pp = net.res_trafo.at[trafo_idx, 'ql_mvar']
Q_loss_calc = Q_hv_calc + Q_lv_calc

print(f"\n--- Pertes/Consommation réactives ---")
print(f"Q_loss (pandapower) = {Q_loss_pp:.4f} MVAr")
print(f"Q_loss (calcul)     = {Q_loss_calc:.4f} MVAr")
print(f"Erreur              = {abs(Q_loss_pp - Q_loss_calc):.6f} MVAr")

# ========================================
# C. PERTES CUIVRE THÉORIQUES
# ========================================

print(f"\n{'='*60}")
print(f"PERTES CUIVRE THÉORIQUES")
print(f"{'='*60}")

# Paramètres du transformateur
vkr_percent = net.trafo.at[trafo_idx, 'vkr_percent']
vk_percent = net.trafo.at[trafo_idx, 'vk_percent']

# Résistance équivalente en p.u. (base : S_n du transformateur)
R_pu = vkr_percent / 100

print(f"\n--- Paramètres du transformateur ---")
print(f"vkr = {vkr_percent}%")
print(f"vk  = {vk_percent}%")
print(f"R_pu = {R_pu:.6f} p.u. (sur base {sn_mva} MVA)")

# Courant en p.u. (base : courant nominal du transformateur)
I_base_hv = sn_mva / (np.sqrt(3) * vn_hv_kv)  # en kA
I_hv_pu = I_hv_ka_pp / I_base_hv

print(f"\n--- Courant en p.u. ---")
print(f"I_base (HV) = {I_base_hv:.4f} kA")
print(f"I_hv        = {I_hv_ka_pp:.4f} kA")
print(f"I_hv_pu     = {I_hv_pu:.5f} p.u.")

P_cu_pu = I_hv_pu**2 * R_pu
P_cu_MW = P_cu_pu * sn_mva

print(f"\n--- Pertes cuivre théoriques ---")
print(f"P_cu = I²_pu x R_pu = {I_hv_pu:.5f}² × {R_pu:.6f}")
print(f"P_cu = {P_cu_pu:.6f} p.u.")
print(f"P_cu = {P_cu_MW:.4f} MW")

# ========================================
# D. PERTES FER (magnétisation)
# ========================================

# Pertes fer = Pertes totales - Pertes cuivre
P_fe_calc = P_loss_calc - P_cu_MW

print(f"\n--- Pertes fer (magnétisation) ---")
print(f"P_fe = P_loss - P_cu")
print(f"P_fe = {P_loss_calc:.4f} - {P_cu_MW:.4f}")
print(f"P_fe = {P_fe_calc:.4f} MW")

# Note : pandapower considère pfe_kw = 0 dans vos données
pfe_kw = net.trafo.at[trafo_idx, 'pfe_kw']
print(f"\nNote : pfe_kw (pandapower) = {pfe_kw} kW")
if pfe_kw == 0:
    print("→ Les pertes fer sont négligées dans le modèle pandapower")
    print(f"→ Donc P_loss ≈ P_cu = {P_cu_MW:.4f} MW")

# ========================================
# E. TABLEAU RÉCAPITULATIF
# ========================================

print(f"\n{'='*60}")
print(f"TABLEAU RÉCAPITULATIF")
print(f"{'='*60}")
print(f"{'Grandeur':<30} {'HV':>15} {'LV':>15} {'Pertes':>15}")
print(f"{'-'*75}")
print(f"{'Puissance active (MW)':<30} {P_hv_calc:>15.4f} {P_lv_calc:>15.4f} {P_loss_calc:>15.4f}")
print(f"{'Puissance réactive (MVAr)':<30} {Q_hv_calc:>15.4f} {Q_lv_calc:>15.4f} {Q_loss_calc:>15.4f}")
print(f"{'Puissance apparente (MVA)':<30} {S_hv_calc:>15.4f} {S_lv_calc:>15.4f} {'-':>15}")
print(f"{'Courant (kA)':<30} {I_hv_ka_pp:>15.4f} {I_lv_ka_pp:>15.4f} {'-':>15}")
print(f"{'Tension (kV)':<30} {V_hv_kV:>15.3f} {V_lv_kV:>15.3f} {'-':>15}")
print(f"{'-'*75}")
print(f"{'Pertes cuivre (MW)':<30} {'-':>15} {'-':>15} {P_cu_MW:>15.4f}")
print(f"{'Pertes fer (MW)':<30} {'-':>15} {'-':>15} {P_fe_calc:>15.4f}")
print(f"{'='*75}")

# ========================================
# F. VÉRIFICATIONS ET INTERPRÉTATION
# ========================================

print(f"\n{'='*60}")
print(f"INTERPRÉTATION PHYSIQUE")
print(f"{'='*60}")

# Vérification de la cohérence
coherence = abs(P_loss_calc - P_cu_MW) < 0.1

print(f"\n--- Cohérence des pertes ---")
print(f"P_loss (calculé)      = {P_loss_calc:.4f} MW")
print(f"P_cu (théorique)      = {P_cu_MW:.4f} MW")
print(f"Différence            = {abs(P_loss_calc - P_cu_MW):.6f} MW")
print(f"Cohérence (< 0.1 MW) : {'OUI' if coherence else 'NON'}")

# Interprétation des pertes réactives
print(f"\n--- Puissance réactive ---")
if Q_loss_calc > 0:
    print(f"Le transformateur CONSOMME {Q_loss_calc:.4f} MVAr")
    print("Effet inductif de la réactance de fuite")
else:
    print(f"Le transformateur GÉNÈRE {abs(Q_loss_calc):.4f} MVAr")
    print("Effet capacitif (rare pour un transformateur)")

# Rendement du transformateur
eta = (P_lv_calc / P_hv_calc) * 100 if P_hv_calc != 0 else 0
print(f"\n--- Rendement ---")
print(f"η = P_LV / P_HV = {P_lv_calc:.4f} / {P_hv_calc:.4f}")
print(f"η = {eta:.3f}%")

# Taux de charge
loading_percent = (S_hv_calc / sn_mva) * 100
print(f"\n--- Taux de charge ---")
print(f"Loading = S_HV / S_n = {S_hv_calc:.4f} / {sn_mva}")
print(f"Loading = {loading_percent:.2f}%")

if loading_percent < 100:
    print(f"Le transformateur fonctionne en sécurité")
elif loading_percent < 110:
    print(f"Le transformateur est proche de sa limite")
else:
    print(f"SURCHARGE ! Le transformateur dépasse sa capacité")

print(f"\n{'='*60}\n")

# ========================================
# Q1.7 : COURANTS PRIMAIRE ET SECONDAIRE + CHARGE NOMINALE
# ========================================

print(f"\n{'='*60}")
print(f"Q1.7 : COURANTS ET FACTEUR DE CHARGE DU TRANSFORMATEUR {trafo_name}")
print(f"{'='*60}")

# ========================================
# A. COURANT CÔTÉ PRIMAIRE (HV)
# ========================================

print(f"\n--- COURANT CÔTÉ PRIMAIRE (HV) ---")

# Données pandapower
I_hv_ka_pp = net.res_trafo.at[trafo_idx, 'i_hv_ka']
print(f"I_HV (pandapower) = {I_hv_ka_pp:.4f} kA")

# Calcul manuel : I_HV = |S_HV| / (√3 × V_HV)
S_hv_calc_MVA = np.sqrt(P_hv_calc**2 + Q_hv_calc**2)
V_hv_kV = V_hv_pu * vn_hv_kv

I_hv_calc_kA = S_hv_calc_MVA / (np.sqrt(3) * V_hv_kV)

print(f"\n--- Calcul manuel : I_HV = |S_HV| / (√3 × V_HV) ---")
print(f"|S_HV|      = √(P² + Q²) = √({P_hv_calc:.4f}² + {Q_hv_calc:.4f}²)")
print(f"|S_HV|      = {S_hv_calc_MVA:.4f} MVA")
print(f"V_HV        = {V_hv_pu:.5f} × {vn_hv_kv} = {V_hv_kV:.3f} kV")
print(f"\nI_HV        = {S_hv_calc_MVA:.4f} / (√3 × {V_hv_kV:.3f})")
print(f"I_HV        = {S_hv_calc_MVA:.4f} / {np.sqrt(3) * V_hv_kV:.3f}")
print(f"I_HV (calcul) = {I_hv_calc_kA:.4f} kA")

# Erreur
err_I_hv = abs(I_hv_calc_kA - I_hv_ka_pp)
err_I_hv_pct = (err_I_hv / I_hv_ka_pp) * 100

print(f"\nErreur      = {err_I_hv:.6f} kA ({err_I_hv_pct:.3f}%)")

# ========================================
# B. COURANT CÔTÉ SECONDAIRE (LV)
# ========================================

print(f"\n{'='*60}")
print(f"--- COURANT CÔTÉ SECONDAIRE (LV) ---")

# Données pandapower
I_lv_ka_pp = net.res_trafo.at[trafo_idx, 'i_lv_ka']
print(f"I_LV (pandapower) = {I_lv_ka_pp:.4f} kA")
S_lv_calc_MVA = np.sqrt(P_lv_calc**2 + Q_lv_calc**2)
V_lv_kV = V_lv_pu * vn_lv_kv

I_lv_calc_kA = S_lv_calc_MVA / (np.sqrt(3) * V_lv_kV)

print(f"\n--- Calcul manuel ---")
print(f"|S_LV|      = sqrt(P² + Q²) = √({P_lv_calc:.4f}² + {Q_lv_calc:.4f}²)")
print(f"|S_LV|      = {S_lv_calc_MVA:.4f} MVA")
print(f"V_LV        = {V_lv_pu:.5f} × {vn_lv_kv} = {V_lv_kV:.3f} kV")
print(f"\nI_LV        = {S_lv_calc_MVA:.4f} / (√3 × {V_lv_kV:.3f})")
print(f"I_LV        = {S_lv_calc_MVA:.4f} / {np.sqrt(3) * V_lv_kV:.3f}")
print(f"I_LV (calcul) = {I_lv_calc_kA:.4f} kA")

# Erreur
err_I_lv = abs(I_lv_calc_kA - I_lv_ka_pp)
err_I_lv_pct = (err_I_lv / I_lv_ka_pp) * 100

print(f"\nErreur      = {err_I_lv:.6f} kA ({err_I_lv_pct:.3f}%)")

# ========================================
# C. COURANTS NOMINAUX (RATED)
# ========================================

print(f"\n{'='*60}")
print(f"--- COURANTS NOMINAUX ---")

# Puissance nominale du transformateur
S_n_MVA = sn_mva
I_rated_hv_kA = S_n_MVA / (np.sqrt(3) * vn_hv_kv)
I_rated_lv_kA = S_n_MVA / (np.sqrt(3) * vn_lv_kv)

print(f"\nPuissance nominale : S_n = {S_n_MVA} MVA")

print(f"\n--- Côté HV ---")
print(f"I_rated_HV = S_n / (√3 × V_nom_HV)")
print(f"I_rated_HV = {S_n_MVA} / (√3 × {vn_hv_kv})")
print(f"I_rated_HV = {S_n_MVA} / {np.sqrt(3) * vn_hv_kv:.3f}")
print(f"I_rated_HV = {I_rated_hv_kA:.4f} kA")

print(f"\n--- Côté LV ---")
print(f"I_rated_LV = S_n / (√3 × V_nom_LV)")
print(f"I_rated_LV = {S_n_MVA} / (√3 × {vn_lv_kv})")
print(f"I_rated_LV = {S_n_MVA} / {np.sqrt(3) * vn_lv_kv:.3f}")
print(f"I_rated_LV = {I_rated_lv_kA:.4f} kA")

# ========================================
# D. FACTEUR DE CHARGE (LOADING)
# ========================================

print(f"\n{'='*60}")
print(f"--- FACTEUR DE CHARGE (LOADING) ---")

# Loading côté HV : loading_HV = |I_HV| / I_rated_HV
loading_hv_calc = (I_hv_calc_kA / I_rated_hv_kA) * 100

# Loading côté LV : loading_LV = |I_LV| / I_rated_LV
loading_lv_calc = (I_lv_calc_kA / I_rated_lv_kA) * 100

print(f"\n--- Côté HV ---")
print(f"Loading_HV = |I_HV| / I_rated_HV")
print(f"Loading_HV = {I_hv_calc_kA:.4f} / {I_rated_hv_kA:.4f}")
print(f"Loading_HV = {loading_hv_calc:.2f}%")

print(f"\n--- Côté LV ---")
print(f"Loading_LV = |I_LV| / I_rated_LV")
print(f"Loading_LV = {I_lv_calc_kA:.4f} / {I_rated_lv_kA:.4f}")
print(f"Loading_LV = {loading_lv_calc:.2f}%")

# Loading depuis pandapower
loading_pp = net.res_trafo.at[trafo_idx, 'loading_percent']
print(f"\n--- Pandapower ---")
print(f"Loading (pandapower) = {loading_pp:.2f}%")

# Erreur
err_loading = abs(loading_hv_calc - loading_pp)
print(f"Erreur = {err_loading:.3f}%")

# ========================================
# E. VÉRIFICATION DU RAPPORT DE TRANSFORMATION
# ========================================

print(f"\n{'='*60}")
print(f"--- VÉRIFICATION DU RAPPORT DE TRANSFORMATION ---")

# Rapport théorique : I_HV / I_LV ≈ V_LV / V_HV (en négligeant les pertes)
rapport_courants = I_lv_calc_kA / I_hv_calc_kA
rapport_tensions = vn_hv_kv / vn_lv_kv

print(f"\nRapport des courants : I_LV / I_HV = {I_lv_calc_kA:.4f} / {I_hv_calc_kA:.4f}")
print(f"                                    = {rapport_courants:.4f}")

print(f"\nRapport de transformation : V_HV / V_LV = {vn_hv_kv} / {vn_lv_kv}")
print(f"                                         = {rapport_tensions:.4f}")

ecart_rapport = abs(rapport_courants - rapport_tensions)
print(f"\nÉcart = {ecart_rapport:.6f}")

if ecart_rapport < 0.1:
    print("Cohérence : I_LV / I_HV ≈ V_HV / V_LV (loi du transformateur)")
else:
    print("Écart significatif dû aux pertes et au déphasage")

# ========================================
# F. TABLEAU RÉCAPITULATIF
# ========================================

print(f"\n{'='*60}")
print(f"TABLEAU RÉCAPITULATIF")
print(f"{'='*60}")
print(f"{'Grandeur':<30} {'HV':>20} {'LV':>20}")
print(f"{'-'*70}")
print(f"{'Tension nominale (kV)':<30} {vn_hv_kv:>20.1f} {vn_lv_kv:>20.1f}")
print(f"{'Tension réelle (kV)':<30} {V_hv_kV:>20.3f} {V_lv_kV:>20.3f}")
print(f"{'Puissance apparente (MVA)':<30} {S_hv_calc_MVA:>20.4f} {S_lv_calc_MVA:>20.4f}")
print(f"{'-'*70}")
print(f"{'Courant calculé (kA)':<30} {I_hv_calc_kA:>20.4f} {I_lv_calc_kA:>20.4f}")
print(f"{'Courant pandapower (kA)':<30} {I_hv_ka_pp:>20.4f} {I_lv_ka_pp:>20.4f}")
print(f"{'Erreur (kA)':<30} {err_I_hv:>20.6f} {err_I_lv:>20.6f}")
print(f"{'-'*70}")
print(f"{'Courant nominal (kA)':<30} {I_rated_hv_kA:>20.4f} {I_rated_lv_kA:>20.4f}")
print(f"{'Facteur de charge (%)':<30} {loading_hv_calc:>20.2f} {loading_lv_calc:>20.2f}")
print(f"{'='*70}")


# ========================================
# Q1.8 : FACTEUR DE PUISSANCE AU NOEUD Ne
# ========================================

print(f"\n{'='*60}")
print(f"Q1.8 : FACTEUR DE PUISSANCE AU NOEUD Ne")
print(f"{'='*60}")

Ne = N203
bus_name = net.bus.at[Ne, 'name']
print(f"\nNœud étudié : {bus_name}")

# ========================================
# A. IDENTIFICATION DE LA CHARGE ET DU SHUNT
# ========================================
loads_at_bus = net.load[net.load['bus'] == Ne]

if len(loads_at_bus) == 0:
    print(f"\nATTENTION : Aucune charge trouvée au nœud {bus_name}")
    print("Vérifiez que le nœud choisi est correct.")
else:
    load_idx = loads_at_bus.index[0]
    load_name = net.load.at[load_idx, 'name']
    P_load_MW = net.load.at[load_idx, 'p_mw']
    Q_load_MVAr = net.load.at[load_idx, 'q_mvar']
    
    print(f"\n--- Charge au nœud {bus_name} ---")
    print(f"Nom de la charge : {load_name}")
    print(f"P_load = {P_load_MW:.2f} MW")
    print(f"Q_load = {Q_load_MVAr:.2f} MVAr")

shunts_at_bus = net.shunt[net.shunt['bus'] == Ne]

if len(shunts_at_bus) == 0:
    print(f"\nATTENTION : Aucun shunt trouvé au nœud {bus_name}")
    Q_shunt_MVAr = 0.0
    has_shunt = False
else:
    shunt_idx = shunts_at_bus.index[0]
    Q_shunt_MVAr = net.shunt.at[shunt_idx, 'q_mvar']
    has_shunt = True
    
    print(f"\n--- Compensateur shunt au nœud {bus_name} ---")
    print(f"Q_shunt = {Q_shunt_MVAr:.2f} MVAr")
    print(f"Type : {'Capacitif (génération)' if Q_shunt_MVAr < 0 else 'Inductif (absorption)'}")

# ========================================
# B. FACTEUR DE PUISSANCE SANS COMPENSATION
# ========================================

print(f"\n{'='*60}")
print(f"--- FACTEUR DE PUISSANCE SANS COMPENSATION ---")
print(f"{'='*60}")

# Sans compensation : seule la charge
P_net_without = P_load_MW
Q_net_without = Q_load_MVAr

# Puissance apparente
S_net_without = np.sqrt(P_net_without**2 + Q_net_without**2)

# Facteur de puissance
PF_without = P_net_without / S_net_without if S_net_without != 0 else 0

# Angle de déphasage
phi_without_rad = np.arctan2(Q_net_without, P_net_without)
phi_without_deg = np.rad2deg(phi_without_rad)

print(f"\n--- Calcul ---")
print(f"P_net = {P_net_without:.2f} MW")
print(f"Q_net = {Q_net_without:.2f} MVAr")
print(f"S_net = sqrt(P² + Q²) = √({P_net_without:.2f}² + {Q_net_without:.2f}²)")
print(f"S_net = {S_net_without:.2f} MVA")
print(f"\nPF = P / S = {P_net_without:.2f} / {S_net_without:.2f}")
print(f"PF (sans compensation) = {PF_without:.4f}")
print(f"Angle phi = arctan(Q/P) = {phi_without_deg:.2f}°")

# Nature de la charge
nature_without = "inductif (en retard)" if Q_net_without > 0 else "capacitif (en avance)"
print(f"\nNature : Facteur de puissance {nature_without}")

# ========================================
# C. FACTEUR DE PUISSANCE AVEC COMPENSATION
# ========================================

print(f"\n{'='*60}")
print(f"--- FACTEUR DE PUISSANCE AVEC COMPENSATION ---")
print(f"{'='*60}")

if not has_shunt:
    print("\nPas de compensateur shunt → PF identique")
    PF_with = PF_without
    phi_with_deg = phi_without_deg
    S_net_with = S_net_without
    Q_net_with = Q_net_without
else:
    # Avec compensation : Q_net = Q_load + Q_shunt
    P_net_with = P_load_MW  # La puissance active ne change pas
    Q_net_with = Q_load_MVAr + Q_shunt_MVAr
    
    # Puissance apparente
    S_net_with = np.sqrt(P_net_with**2 + Q_net_with**2)
    
    # Facteur de puissance
    PF_with = P_net_with / S_net_with if S_net_with != 0 else 0
    
    # Angle de déphasage
    phi_with_rad = np.arctan2(Q_net_with, P_net_with)
    phi_with_deg = np.rad2deg(phi_with_rad)
    
    print(f"\n--- Calcul ---")
    print(f"P_net = {P_net_with:.2f} MW (inchangé)")
    print(f"Q_net = Q_load + Q_shunt")
    print(f"Q_net = {Q_load_MVAr:.2f} + ({Q_shunt_MVAr:.2f})")
    print(f"Q_net = {Q_net_with:.2f} MVAr")
    print(f"\nS_net = sqrt(P² + Q²) = √({P_net_with:.2f}² + {Q_net_with:.2f}²)")
    print(f"S_net = {S_net_with:.2f} MVA")
    print(f"\nPF = P / S = {P_net_with:.2f} / {S_net_with:.2f}")
    print(f"PF (avec compensation) = {PF_with:.4f}")
    print(f"Angle phi = arctan(Q/P) = {phi_with_deg:.2f}°")
    
    # Nature de la charge
    nature_with = "inductif (en retard)" if Q_net_with > 0 else "capacitif (en avance)"
    print(f"\nNature : Facteur de puissance {nature_with}")

# ========================================
# D. COMPARAISON ET ANALYSE
# ========================================

print(f"\n{'='*60}")
print(f"--- COMPARAISON ---")
print(f"{'='*60}")

print(f"\n{'Paramètre':<30} {'Sans compensation':>20} {'Avec compensation':>20}")
print(f"{'-'*70}")
print(f"{'P (MW)':<30} {P_net_without:>20.2f} {P_net_with:>20.2f}")
print(f"{'Q (MVAr)':<30} {Q_net_without:>20.2f} {Q_net_with:>20.2f}")
print(f"{'S (MVA)':<30} {S_net_without:>20.2f} {S_net_with:>20.2f}")
print(f"{'Facteur de puissance':<30} {PF_without:>20.4f} {PF_with:>20.4f}")
print(f"{'Angle φ (°)':<30} {phi_without_deg:>20.2f} {phi_with_deg:>20.2f}")
print(f"{'='*70}")

if has_shunt:
    # Amélioration du facteur de puissance
    delta_PF = PF_with - PF_without
    improvement_pct = (delta_PF / PF_without) * 100
    
    # Réduction de la puissance réactive
    delta_Q = abs(Q_net_with) - abs(Q_net_without)
    reduction_Q_pct = (delta_Q / abs(Q_net_without)) * 100 if Q_net_without != 0 else 0
    
    # Réduction de la puissance apparente
    delta_S = S_net_with - S_net_without
    reduction_S_pct = (delta_S / S_net_without) * 100
    
    print(f"\n--- Effet de la compensation ---")
    print(f"PF = {delta_PF:+.4f} ({improvement_pct:+.2f}%)")
    print(f"dQ  = {delta_Q:+.2f} MVAr ({reduction_Q_pct:+.2f}%)")
    print(f"dS  = {delta_S:+.2f} MVA ({reduction_S_pct:+.2f}%)")
    
    if delta_PF > 0:
        print(f"\nLe compensateur shunt AMÉLIORE le facteur de puissance")
        print(f"Réduction de la puissance réactive de {abs(reduction_Q_pct):.1f}%")
        print(f"Réduction de la puissance apparente de {abs(reduction_S_pct):.1f}%")
    else:
        print(f"\nLe compensateur shunt DÉGRADE le facteur de puissance")

# ========================================
# E. VÉRIFICATION AVEC PANDAPOWER
# ========================================

print(f"\n{'='*60}")
print(f"--- VÉRIFICATION AVEC PANDAPOWER ---")
print(f"{'='*60}")

# Résultats du load flow au bus
V_bus_pu = net.res_bus.at[Ne, 'vm_pu']
P_bus_MW = net.res_bus.at[Ne, 'p_mw']  # Puissance active nette au bus
Q_bus_MVAr = net.res_bus.at[Ne, 'q_mvar']  # Puissance réactive nette au bus

print(f"\n--- Résultats pandapower au bus {bus_name} ---")
print(f"Tension : {V_bus_pu:.5f} p.u.")
print(f"P_bus   : {P_bus_MW:.2f} MW")
print(f"Q_bus   : {Q_bus_MVAr:.2f} MVAr")

S_bus_MVA = np.sqrt(P_bus_MW**2 + Q_bus_MVAr**2)
PF_bus = abs(P_bus_MW) / S_bus_MVA if S_bus_MVA != 0 else 0

print(f"S_bus   : {S_bus_MVA:.2f} MVA")
print(f"PF_bus  : {PF_bus:.4f}")

print(f"\nNote : Les résultats pandapower incluent tous les éléments")
print(f"connectés au bus (charge + shunt + flux réseaux)")


