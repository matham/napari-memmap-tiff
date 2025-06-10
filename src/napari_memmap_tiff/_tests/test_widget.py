from napari_memmap_tiff._widget import memmap_config_widget


def test_memmap_config_widget():
    from imageio.config.plugins import known_plugins

    memmap_config_widget(True)
    assert "tifffile_memmap" in known_plugins
    memmap_config_widget(False)
    assert "tifffile_memmap" not in known_plugins
