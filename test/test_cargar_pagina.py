import pytest
from pages.pages_compra import CargaPagina
from selenium import webdriver


class TestCargarPagina:
    def test_carga_tienda_nube(self, driver:webdriver.Remote):
        cargar_pagina = CargaPagina(driver)
        driver.get("https://pruebasautomation.mitiendanube.com/productos/guante-wilson/")