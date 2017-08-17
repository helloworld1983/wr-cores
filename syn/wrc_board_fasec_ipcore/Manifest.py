target = "xilinx"
action = "synthesis"

syn_device = "xc7z030"
syn_grade = "-2"
syn_package = "ffg676"

syn_top = "wrc_board_fasec"
syn_project = "fasec_wr_ref_top"

syn_tool = "vivado"

modules = { "local" : [
                "../../",
                "../../board/fasec/" ] }
