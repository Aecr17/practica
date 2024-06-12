import pytest
from pages.pages_compra import CargaPagina
from pages.agregar_producto_page import AgregarProducto
from pages.page_carrito import VerCarrito
from selenium import webdriver

class TestCarritoCompras:
    def test_carga_tienda_nube(self, driver:webdriver.Remote):
        cargar_pagina = CargaPagina(driver)
        agregar_producto = AgregarProducto(driver)
        observar_carrito = VerCarrito(driver)
        driver.get("https://pruebasautomation.mitiendanube.com/productos/guante-wilson/")
        agregar_producto.interactuar_cookies()
        agregar_producto.agregar_producto()
        observar_carrito.carrito_compras()
        