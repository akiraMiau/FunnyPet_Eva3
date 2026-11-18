-- ==========================================================
-- SCRIPT DE BASE DE DATOS - PROYECTO FUNNYPET STORE
-- ==========================================================

CREATE DATABASE IF NOT EXISTS `funnypet_db` 
DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE `funnypet_db`;

-- 1. Creación de la tabla Padre: tienda_categoria
CREATE TABLE `tienda_categoria` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 2. Creación de la tabla Hija: tienda_producto
CREATE TABLE `tienda_producto` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `fecha_ingreso` date NOT NULL,
  `stock_prod` int NOT NULL,
  `disponible` tinyint(1) NOT NULL,
  `categoria_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Tienda_producto_categoria_id_040deec3_fk_Tienda_categoria_id` (`categoria_id`),
  CONSTRAINT `Tienda_producto_categoria_id_040deec3_fk_Tienda_categoria_id` FOREIGN KEY (`categoria_id`) REFERENCES `tienda_categoria` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ==========================================================
-- CONSULTAS DE VERIFICACIÓN E INTEGRIDAD RELACIONAL
-- ==========================================================

-- Conteo de entidades padre (Categorías)
SELECT COUNT(*) AS total_padres FROM tienda_categoria;

-- Conteo de entidades hijas (Productos)
SELECT COUNT(*) AS total_hijos FROM tienda_producto;

-- Consulta relacional con INNER JOIN
SELECT h.id, h.nombre, p.nombre AS clasificacion
FROM tienda_producto h
INNER JOIN tienda_categoria p ON h.categoria_id = p.id;