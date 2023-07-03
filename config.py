from pathlib import Path

out_path_override = Path('.out_path_override')
out_path = Path(out_path_override.read_text().strip() if out_path_override.exists() else '.')
index_of_hashes_out_path = out_path / 'hashes'

updates_unsupported = {}

updates_max_age_days = 60
updates_never_removed = False
allow_missing_sha256_hash = True
allow_unknown_non_pe_files = True

verbose_run = False
verbose_progress = True
extract_in_a_new_thread = False
exit_on_first_error = True
high_mem_usage_for_performance = False
compression_level = 3

delta_machine_type_values_supported = {
    'CLI4_I386',
    'CLI4_AMD64',
    'CLI4_ARM',
    'CLI4_ARM64',
}

# Non-PE files (very rare).
file_hashes_non_pe = {
    'af700c04f4334cdf9fc575727a055a30855e1ab6a8a480ab6335e1b4a7585173',  # tapi.dll
}

tcb_launcher_descriptions = ['TCB Launcher', 'TCB Launcher (Prerelease)']
tcb_launcher_large_first_section_virtual_addresses = [0x1000, 0x3000, 0x4000, 0x6000]

file_hashes_unusual_section_alignment = {
    'ede86c8d8c6b9256b926701f4762bd6f71e487f366dfc7db8d74b8af57e79bbb': {'first_section_virtual_address': 0x380, 'section_alignment': 0x80},  # ftdibus.sys
    '5bec55192eaef43b0fade13bbadfdf77eb0d45b4b281ae19d4b0b7a0c2350836': {'first_section_virtual_address': 0x2d0, 'section_alignment': 0x10},  # onnxruntime.dll
    '09ced31cad8547a9ee5dcf739565def2f4359075e56a7b699cc85971e0905864': {'first_section_virtual_address': 0x310, 'section_alignment': 0x10},  # onnxruntime.dll
    '3b0a51e1fc4d5bd3e7ec182799ad712aeeaf1dcd761d7e98bec8a0a67f7334af': {'first_section_virtual_address': 0x380, 'section_alignment': 0x80},  # e1g6032e.sys
    '7ae7316c42b47d29f72ea0618c8f2641b412a74dcc707f91e6fd9e156901fd65': {'first_section_virtual_address': 0x600, 'section_alignment': 0x200},  # e100b325.sys
    '75d5318e35813a6b6a9a17734877e6fb7ce31b415e91914c92d86e3da0a4ffb5': {'first_section_virtual_address': 0x600, 'section_alignment': 0x200},  # e1g60i32.sys
    '2dbfff4b7bc30453830523e1bdc8737dd6101102b2e178d4fabd051ff8d01dd4': {'first_section_virtual_address': 0x300, 'section_alignment': 0x80},  # efe5b32e.sys
    'cbd4667fd69c6d40118ea25cafde663a1fe4ca203fb7135e65f682d77a85a3b9': {'first_section_virtual_address': 0x480, 'section_alignment': 0x80},  # nvm62x32.sys
    '50256eeadbbc5cccf3ebaeb9020d91edb9961e7404bd41067a4290362be6962f': {'first_section_virtual_address': 0x380, 'section_alignment': 0x80},  # nvm62x64.sys
}

file_hashes_zero_timestamp = {
    '18dd945c04ce0fbe882cd3f234c2da2d0faa12b23bd6df7b1edc31faecf51c69',  # brlapi-0.8.dll
    '7a9113d00a274c075c58b22a3ebacf1754e7da7cfb4d3334b90367b602158d78',  # brltty.exe
}

file_hashes_small_non_signature_overlay = {
    '11efef27aea856060bdeb6d2f0d62c68088eb891997d4e99de708a6b51743148',  # brlapi-0.6.dll
    'b175123eff88d1573f451b286cd5370003a0839e53c7ae86bf22b35b7e77bad3',  # brlapi-0.6.dll
    '18dd945c04ce0fbe882cd3f234c2da2d0faa12b23bd6df7b1edc31faecf51c69',  # brlapi-0.8.dll
    '3eaa62334520b41355c5103dcd663744ba26caae3496bd9015bc399fbaf42fce',  # brltty.exe
    '69f83db2fda7545ab0a1c60056aee472bf3c70a0af7454c51e1cd449b5c7f43b',  # brltty.exe
    '7a9113d00a274c075c58b22a3ebacf1754e7da7cfb4d3334b90367b602158d78',  # brltty.exe
    'b4cc93cf4d7c2906c1929c079cd98ef00c7a33832e132ac57adde71857082e36',  # libgcc_s_dw2-1.dll
    'f6f4951f98185ba8ddcdaa43f13b8106b9b667bb7f5ee027dc51b4bca4556adc',  # crtdll.dll
    'e9c61945c0c7b887ec786832af1056334968d890fc042f0c16b8d7f80a2c0c9a',  # expsrv.dll
    '078d2cd98918638f40ce0f1fc0c3c9079ee1a6fbd3b45d6c32ab99fda642efe9',  # vbajet32.dll
    '25681fc405354e54c08e91d2d1cc3212dd17db7cb1fc85c3cb7eee73ab3bbdc8',  # vbajet32.dll
}

file_hashes_unsigned_with_overlay = {
    'cf54a8504f2dbdd7bea3acdcd065608d21f5c06924baf647955cc28b8637ae68',  # libiconv-2.dll
    'ee1df918ca67581f21eac49ae4baffca959f71d1a0676d7c35bc5fb96bea3a48',  # libiconv-2.dll
    '9eec7e5188d1a224325281e4d0e6e1d5f9f034f02bd1fadeb792d3612c72319e',  # libpdcurses.dll
    'f9b385e19b9d57a1d1831e744ed2d1c3bb8396d28f48d10120cecfe72595b222',  # libpdcursesu.dll
    '787d5c07ab0bb782dede7564840e86c468e3728e81266dae23eb8ad614bcee95',  # libpdcursesw.dll
    '6896c1f21cc9a5bc17e2e2fb645669ae708cb378c63e5eef11b3e95527f3da32',  # ctl3d32.dll
    '94ef91b4c7864bd1ecc0db099e58298708bc5d22da40132ebb1c17feb4675964',  # ctl3d32.dll
    'c8aacb7314fe061b16c0d1961f4071e144be9aa44e7e00cd89b9b6581aad6430',  # mfc40.dll
    '3ca65b6f8fca231a266248fe6f67b6a87568ba1dcf810eef355d7699f603aa22',  # mfc40u.dll
    '3b2f5858bc5181506e84f6fa09eb755fb5b5e87f48c838bb125eb01fa13cf17e',  # msvbvm60.dll
}

file_details_unsigned_with_overlay = [
    {'k': 'original name', 'v': 'WofTasks.dll', 'overlay_size': 0x200},
]

# Details: https://gist.github.com/m417z/3248c18efd942f63013b8d3035e2dc79
file_hashes_mismatch = {
    # Temporary workaround for what seems to be an incorrect SHA256 hash in
    # KB5017389 and newer Windows 11 22H2 update manifests for some of the
    # files. The files are language resource files (e.g. resources.en-GB.pri)
    # for some esoteric apps:
    # * holocamera_cw5n1h2txyewy
    # * MixedRealityLearning_cw5n1h2txyewy
    # * RoomAdjustment_cw5n1h2txyewy
    ('f8636d2d93606b0069117cb05bc8d91ecb9a09e72e14695d56a693adf419f4e8', '70db27fdd0fd76305fb1dfcd401e8cde'): {'11-22H2'},
    ('5ca0a43e4be5f7b60cd2170b05eb4627407729c65e7e0b62ed4ef3cdf895f5c5', '6ad932076c6a059db6e9743ae06c62cf'): {'11-22H2'},
    ('b5a73db6c73c788dd62a1e5c0aa7bc2f50a260d52b04fcec4cd0192a25c6658f', 'af8a7f7b812a40bf8a1c151d3f09a98c'): {'11-22H2'},
    ('d52440f126d95e94a86465e78849a72df11f0c22115e5b8cda10174d69167a44', 'afbb5df39d32d142a4cca08f89bbbe8e'): {'11-22H2'},
    ('5a3b750a6dcc984084422d5c28ac99a2f878fdfe26c7261c9bff8de77658e8f8', '7ed0e64f81f63730983913be5b3cce17'): {'11-22H2'},
    ('5292013c895e0f412c98766ba4ed7ba5ecb24bebf00aac5b56c71bcf44891945', '886ee85f216e28ac547fe71ff2823fc4'): {'11-22H2'},
    ('b9297098632fbb1a513f96d6d2462926144d6528c4cc426d6caed5ed234438f0', '19aabb40b6431f411f97c85fbe77d7fe'): {'11-22H2'},
    ('700760afebec6b3d638adac2f1cbb96cb60fbe9a2e2558eb20a63f9ebbd2c74f', '1f91bbe1b8ec8c42f00ffc73cbb72247'): {'11-22H2'},
    ('994274f4494a852c0fe8c968d054fbaf0f6f7489ea586fc84102c6ebcafeeca3', 'a0d4e4256e8d54ab86ac6505f1272219'): {'11-22H2'},
    # wfascim_uninstall.mof in KB5025298 and newer Windows 11 21H2 updates.
    ('cee501be4532071c6fe1df2933d98f8fccba4803de481746808386c3245ad6a7', '9e51833f306f8c5c59bc8f041a9ec1bb'): {'11-21H2'},
}
