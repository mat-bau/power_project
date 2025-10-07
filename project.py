import pandapower as pp
import pandapower.control as ct


def My_Amazing_Grid():

    net = pp.create_empty_network(f_hz=50, sn_mva=100)
    # Custom transformer types
    pp.create_std_type(net, 
                       {"sn_mva": 1000.0, "vn_hv_kv": 380.0, 
                        "vn_lv_kv": 20.0, "vk_percent": 10.0, 
                        "vkr_percent": 0.2, "pfe_kw": 0, 
                        "i0_percent": 0.0, "shift_degree": 0.0, 
                        "tap_side": "hv", "tap_neutral": 0, 
                        "tap_min": -20, "tap_max": 20, 
                        "tap_step_percent": 1, "tap_step_degree": 0, 
                        "tap_phase_shifter": False}, name="_20kV_380kV_type", element='trafo')
    pp.create_std_type(net, 
                       {"sn_mva": 550.0, "vn_hv_kv": 380.0, 
                        "vn_lv_kv": 150.0, "vk_percent": 22.0, 
                        "vkr_percent": 0.25, "pfe_kw": 0, 
                        "i0_percent": 0.0, "shift_degree": 0.0,
                        "tap_side": "hv", "tap_neutral": 0, 
                        "tap_min": -20, "tap_max": 20, 
                        "tap_step_percent": 1, "tap_step_degree": 0, 
                        "tap_phase_shifter": False}, name="_150kV_380kV_type", element='trafo')
    pp.create_std_type(net, 
                       {"sn_mva": 500.0, "vn_hv_kv": 150.0, 
                        "vn_lv_kv": 15.0, "vk_percent": 12.0, 
                        "vkr_percent": 0.28, "pfe_kw": 0, 
                        "i0_percent": 0.0, "shift_degree": 0.0, 
                        "tap_side": "lv", "tap_neutral": 0, 
                        "tap_min": -4, "tap_max": 20, 
                        "tap_step_percent": 1.0, "tap_step_degree": 0, 
                        "tap_phase_shifter": False}, name="_15kV_150kV_type", element='trafo')
    pp.create_std_type(net, 
                       {"sn_mva": 500.0, "vn_hv_kv": 150.0, 
                        "vn_lv_kv": 20.0, "vk_percent": 13.0, 
                        "vkr_percent": 0.25, "pfe_kw": 0, 
                        "i0_percent": 0.0, "shift_degree": 0.0, 
                        "tap_side": "hv", "tap_neutral": 0, 
                        "tap_min": -20, "tap_max": 20, 
                        "tap_step_percent": 1, "tap_step_degree": 0, 
                        "tap_phase_shifter": False}, name="_20kV_150kV_type", element='trafo')

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
    

    # Grid 1 - Tilmans-------------------------------------------------------------------------------

    # Création busses
    B27 = pp.create_bus(net, vn_kv=380, name="B27")
    B28 = pp.create_bus(net, vn_kv=380, name="B28")
    B29 = pp.create_bus(net, vn_kv=20, name="B29")
    B30 = pp.create_bus(net, vn_kv=380, name="B30")
    B31 = pp.create_bus(net, vn_kv=380, name="B31")
    B32 = pp.create_bus(net, vn_kv=380, name="B32")
    B33 = pp.create_bus(net, vn_kv=380, name="B33")
    B34 = pp.create_bus(net, vn_kv=380, name="B34")

    # Création Load
    LOAD_B27 = pp.create_load(net, bus=B27, p_mw=200, q_mvar=50, name="LOAD_B27")
    LOAD_B30 = pp.create_load(net, bus=B30, p_mw=200, q_mvar=50, name="LOAD_B30")
    LOAD_B32 = pp.create_load(net, bus=B32, p_mw=200, q_mvar=50, name="LOAD_B32")
    LOAD_B34 = pp.create_load(net, bus=B34, p_mw=200, q_mvar=50, name="LOAD_B34")

    # Création Tansfo
    TRAFO_B28B29 = pp.create_transformer(net, hv_bus=B28, lv_bus=B29, std_type="_20kV_380kV_type", name="TRAFO_B28B29")

    # Création Gen
    G_B29 = pp.create_gen(net, bus=B29, p_mw=800, max_q_mvar=575, min_q_mvar=-250, sn_mva=1000, vm_pu=1.09, slack=True ,name="G_B29")
    G_B31 = pp.create_gen(net, bus=B31, p_mw=210, max_q_mvar=2000, min_q_mvar=-500, sn_mva=1000, vm_pu=1.09, slack=False ,name="G_B31")
    G_B33 = pp.create_gen(net, bus=B33, p_mw=210, max_q_mvar=2000, min_q_mvar=-500, sn_mva=1000, vm_pu=1.09, slack=False ,name="G_B33")

    # Création Lines
    LINE_B27B28 = pp.create_line(net, from_bus=B27, to_bus=B28, length_km=1, std_type="_380kv_type", name="LINE_B27B28")
    LINE_B28B30 = pp.create_line(net, from_bus=B28, to_bus=B30, length_km=1, std_type="_380kv_type", name="LINE_B28B30")
    LINE_B28B34 = pp.create_line(net, from_bus=B28, to_bus=B34, length_km=1, std_type="_380kv_type", name="LINE_B28B34")
    LINE_B28B32 = pp.create_line(net, from_bus=B28, to_bus=B32, length_km=1, std_type="_380kv_type", name="LINE_B28B32")
    LINE_B31B32 = pp.create_line(net, from_bus=B31, to_bus=B32, length_km=1, std_type="_380kv_type", name="LINE_B31B32")
    LINE_B33B34 = pp.create_line(net, from_bus=B33, to_bus=B34, length_km=1, std_type="_380kv_type", name="LINE_B33B34")


    # Grid 2 - Schupp -------------------------------------------------------------------------------

    # Création busses
    B15 = pp.create_bus(net, vn_kv=20, name="B15")
    B17 = pp.create_bus(net, vn_kv=380, name="B17")
    B18 = pp.create_bus(net, vn_kv=15, name="B18")
    B19 = pp.create_bus(net, vn_kv=150, name="B19")
    B20 = pp.create_bus(net, vn_kv=20, name="B20")
    B21 = pp.create_bus(net, vn_kv=150, name="B21")
    B22 = pp.create_bus(net, vn_kv=15, name="B22")
    B23 = pp.create_bus(net, vn_kv=380, name="B23")

    # Création Generators
    G_B15 = pp.create_gen(net, bus=B15, p_mw=300, max_q_mvar=200, min_q_mvar=-50, sn_mva=450, vm_pu=0.98, slack=False, name="G_B15")
    G_B20 = pp.create_gen(net, bus=B20, p_mw=300, max_q_mvar=200, min_q_mvar=-50, sn_mva=450, vm_pu=0.98, slack=False, name="G_B20")

    # Création Loads
    LOAD_B18 = pp.create_load(net, bus=B18, p_mw=360, q_mvar=180, name="LOAD_B18")
    LOAD_B22 = pp.create_load(net, bus=B22, p_mw=360, q_mvar=180, name="LOAD_B22")

    # Création Shunts
    C_B18 = pp.create_shunt(net, bus=B18, q_mvar=45, p_mw=0, name="C_B18")
    C_B19 = pp.create_shunt(net, bus=B19, q_mvar=75, p_mw=0, name="C_B19")
    C_B21 = pp.create_shunt(net, bus=B21, q_mvar=75, p_mw=0, name="C_B21")
    C_B22 = pp.create_shunt(net, bus=B22, q_mvar=45, p_mw=0, name="C_B22")

    # Création Transformers
    TRAFO_B15B19 = pp.create_transformer(net, hv_bus=B19, lv_bus=B15, std_type="_20kV_150kV_type", name="TRAFO_B15B19")
    TRAFO_B17B19 = pp.create_transformer(net, hv_bus=B17, lv_bus=B19, std_type="_150kV_380kV_type", name="TRAFO_B17B19")
    TRAFO_B18B19 = pp.create_transformer(net, hv_bus=B19, lv_bus=B18, std_type="_15kV_150kV_type", name="TRAFO_B18B19")
    TRAFO_B20B21 = pp.create_transformer(net, hv_bus=B21, lv_bus=B20, std_type="_20kV_150kV_type", name="TRAFO_B20B21")
    TRAFO_B21B22 = pp.create_transformer(net, hv_bus=B21, lv_bus=B22, std_type="_15kV_150kV_type", name="TRAFO_B21B22")
    TRAFO_B21B23 = pp.create_transformer(net, hv_bus=B23, lv_bus=B21, std_type="_150kV_380kV_type", name="TRAFO_B21B23")


    # Grid 3 - Bauvir -------------------------------------------------------------------------------

    # Création busses
    B1 = pp.create_bus(net, vn_kv = 20, name= "B1")
    B2 = pp.create_bus(net, vn_kv = 20, name= "B2")
    B3 = pp.create_bus(net, vn_kv = 20, name= "B3")
    B4 = pp.create_bus(net, vn_kv = 20, name= "B4")
    B5 = pp.create_bus(net, vn_kv = 20, name= "B5")
    B6 = pp.create_bus(net, vn_kv = 20, name= "B6")
    B7 = pp.create_bus(net, vn_kv = 20, name= "B7")
    B8 = pp.create_bus(net, vn_kv = 20, name= "B8")
    B9 = pp.create_bus(net, vn_kv = 20, name= "B9")
    B10 = pp.create_bus(net, vn_kv = 20, name= "B10")
    B11 = pp.create_bus(net, vn_kv = 20, name= "B11")
    B12 = pp.create_bus(net, vn_kv = 20, name= "B12")
    B13 = pp.create_bus(net, vn_kv = 20, name= "B13")
    B14 = pp.create_bus(net, vn_kv = 20, name= "B14")
    B16 = pp.create_bus(net, vn_kv = 20, name= "B16")

    # Création Loads
    LOAD_B1 = pp.create_load(net, B1, p_mw=50, q_mvar=40, name="LOAD_B1")
    LOAD_B4 = pp.create_load(net, B4, p_mw=360, q_mvar=180, name="LOAD_B4")
    LOAD_B7 = pp.create_load(net, B7, p_mw=50, q_mvar=40, name="LOAD_B7")
    LOAD_B11 = pp.create_load(net, B11, p_mw=360, q_mvar=180, name="LOAD_B11")
    LOAD_B14 = pp.create_load(net, B14, p_mw=360, q_mvar=180, name="LOAD_B14")
    LOAD_B16 = pp.create_load(net, B16, p_mw=360, q_mvar=180, name="LOAD_B16")

    # Création Shunts
    C_B4 = pp.create_shunt(net, B4, q_mvar=45, name="C_B4")
    C_B11 = pp.create_shunt(net, B11, q_mvar=45, name="C_B11")
    C_B14 = pp.create_shunt(net, B14, q_mvar=45, name="C_B14")
    C_B16 = pp.create_shunt(net, B16, q_mvar=45, name="C_B16")



    # Création Lines
    LINE_B2B5 = pp.create_line(net, from_bus=B2, to_bus=B5, length_km=1, std_type="_380kV_type", name="LINE_B5B2")

    LINE_B5B6 = pp.create_line(net, from_bus=B5, to_bus=B6, length_km=1, std_type="_20kV_150kV_type", name="LINE_B5B6")
    LINE_B5B6 = pp.create_line(net, from_bus=B5, to_bus=B6, length_km=1, std_type="_20kV_150kV_type", name="LINE_B5B6")
    LINE_B6B9 = pp.create_line(net, from_bus=B6, to_bus=B9, length_km=1, std_type="_20kV_150kV_type", name="LINE_B6B9")
    LINE_B8B13 = pp.create_line(net, from_bus=B8, to_bus=B13, length_km=1, std_type="_20kV_150kV_type", name="LINE_B8B13")
    #LINE_B6B24 = pp.create_line(net, from_bus=B6, to_bus=B24, length_km=1, std_type="_20kV_150kV_type", name="LINE_B6B24")
    #LINE_B6B17 = pp.create_line(net, from_bus=B6, to_bus=B17, length_km=1, std_type="_20kV_150kV_type", name="LINE_B6B17")
    #LINE_B8B19 = pp.create_line(net, from_bus=B8, to_bus=B19, length_km=1, std_type="_20kV_150kV_type", name="LINE_B8B19")
    #LINE_B13B25 = pp.create_line(net, from_bus=B13, to_bus=B25, length_km=1, std_type="_20kV_150kV_type", name="LINE_B13B25")
    LINE_B10B13 = pp.create_line(net, from_bus=B10, to_bus=B13, length_km=1, std_type="_20kV_150kV_type", name="LINE_B10B13")

    # Création Transfo


    # Grid 4 - Tilmans -------------------------------------------------------------------------------

    # Création busses
    B24 = pp.create_bus(net, vn_kv=380, name="B24")
    B25 = pp.create_bus(net, vn_kv=150, name="B25")
    B26 = pp.create_bus(net, vn_kv=15, name="B26")

    # Création Load
    LOAD_B26 = pp.create_load(net, bus=B26, p_mw=360, q_mvar=180, name="LOAD_B26")

    # Création Shunt
    C_B25 = pp.create_shunt(net, bus=B25, q_mvar=-75, p_mw=0, name="C_B25")
    C_B26 = pp.create_shunt(net, bus=B26, q_mvar=-45, p_mw=0, name="C_B26")

    # Création Tansfo
    TRAFO_B24B25 = pp.create_transformer(net, hv_bus=B24, lv_bus=B25, std_type="_150kV_380kV_type", name="TRAFO_B24B25")
    TRAFO_B25B26 = pp.create_transformer(net, hv_bus=B25, lv_bus=B26, std_type="_15kV_150kV_type", name="TRAFO_B25B26")
    
    # Grid 5 - Schupp-------------------------------------------------------------------------------

    # Création busses
    B9 = pp.create_bus(net, vn_kv=380, name="B9")
    B10 = pp.create_bus(net, vn_kv=150, name="B10")
    B11 = pp.create_bus(net, vn_kv=15, name="B11")

    # Création Loads
    LOAD_B11 = pp.create_load(net, bus=B11, p_mw=360, q_mvar=180, name="LOAD_B11")

    # Création Shunts
    C_B11 = pp.create_shunt(net, bus=B11, q_mvar=45, name="C_B11")

    # Création Transformers
    TRAFO_B9B10 = pp.create_transformer(net, hv_bus=B9, lv_bus=B10, std_type="_150kV_380kV_type", name="TRAFO_B9B10")
    TRAFO_B10B11 = pp.create_transformer(net, hv_bus=B10, lv_bus=B11, std_type="_15kV_150kV_type", name="TRAFO_B10B11")

    # Conncections InterGrids-------------------------------------------------------------------------------

    # Sortie Grid 3
    LINE_B6B9_1 = pp.create_line(net, from_bus=6, to_bus=9, length_km=1, std_type="_380kv_type", name="LINE_B6B9_1")
    LINE_B6B9_2 = pp.create_line(net, from_bus=6, to_bus=9, length_km=1, std_type="_380kv_type", name="LINE_B6B9_2")

    LINE_B6B24 = pp.create_line(net, from_bus=6, to_bus=B24, length_km=1, std_type="_380kv_type", name="LINE_B6B24")
    LINE_B6B17 = pp.create_line(net, from_bus=6, to_bus=17, length_km=1, std_type="_380kv_type", name="LINE_B6B17")

    LINE_B8B16 = pp.create_line(net, from_bus=8, to_bus=16, length_km=1, std_type="_150kv_type", name="LINE_B8B16")
    LINE_B10B13 = pp.create_line(net, from_bus=10, to_bus=13, length_km=1, std_type="_150kv_type", name="LINE_B10B13")
    LINE_B13B25 = pp.create_line(net, from_bus=13, to_bus=B25, length_km=1, std_type="_150kv_type", name="LINE_B13B25")

    # Sortie Grid 2
    LINE_B10B21 = pp.create_line(net, from_bus=10, to_bus=21, length_km=1, std_type="_150kv_type", name="LINE_B10B21")
    LINE_B21B25 = pp.create_line(net, from_bus=21, to_bus=B25, length_km=1, std_type="_150kv_type", name="LINE_B21B25")

    LINE_B23B24 = pp.create_line(net, from_bus=23, to_bus=B24, length_km=1, std_type="_380kv_type", name="LINE_B23B24")

    # Sortie de Grid 1
    LINE_B24B27 = pp.create_line(net, from_bus=B24, to_bus=B27, length_km=1, std_type="_380kv_type", name="LINE_B24B27")
    LINE_B24B30 = pp.create_line(net, from_bus=B24, to_bus=B30, length_km=1, std_type="_380kv_type", name="LINE_B24B30")

    # Sortie Grid 4
    # Toutes déjà faites

    # Sortie de Grid 5
    # Toutes déjà faites





    return net