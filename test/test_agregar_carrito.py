import pytest
from pages.pages_compra import CargaPagina
from pages.agregar_producto_page import AgregarProducto
from selenium import webdriver

class TestAgregarCarrito:
    def test_carga_tienda_nube(self, driver:webdriver.Remote):
        cargar_pagina = CargaPagina(driver)
        agregar_producto = AgregarProducto(driver)
        driver.get("https://pruebasautomation.mitiendanube.com/productos/guante-wilson/")
        agregar_producto.interactuar_cookies()
        agregar_producto.agregar_producto()
        