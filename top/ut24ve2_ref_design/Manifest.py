fetchto = "../../ip_cores"

files = [
    "ut24ve2_wr_ref_top.vhd",
    "ut24ve2_wr_ref_top.ucf",
    "ut24ve2_wr_ref_top.bmm",
]

modules = {
    "local" : [
        "../../",
        "../../board/ut24ve2",
    ],
    "git" : [
        "git://ohwr.org/hdl-core-lib/general-cores.git",
        "git://ohwr.org/hdl-core-lib/etherbone-core.git",
    ],
}
