
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";




CREATE TABLE `gastos` (
  `ID` int(3) NOT NULL,
  `Clave` varchar(9) NOT NULL,
  `Nombre` varchar(255) NOT NULL,
  `Medida` varchar(20) NOT NULL,
  `Categoria` varchar(50) NOT NULL,
  `U_Medida` varchar(5) NOT NULL,
  `Cantidad` decimal(11,0) NOT NULL,
  `Proveedor` varchar(50) NOT NULL,
  `Lugar` varchar(100) DEFAULT NULL,
  `TipoMaterial` varchar(50) DEFAULT NULL,
  `Descripcion` varchar(255) NOT NULL,
  `IMG` longblob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;





DELIMITER $$
CREATE TRIGGER `after_gastos_delete` AFTER DELETE ON `gastos` FOR EACH ROW BEGIN
    DELETE FROM min_max WHERE Clave = OLD.Clave;
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `after_gastos_insert` AFTER INSERT ON `gastos` FOR EACH ROW BEGIN
    INSERT INTO min_max (Clave) VALUES (NEW.Clave);
END
$$
DELIMITER ;

CREATE TABLE `historialmovimientos` (
  `ID` int(11) NOT NULL,
  `Descripcion` text DEFAULT NULL,
  `Categoria` varchar(50) DEFAULT NULL,
  `Fecha` date DEFAULT NULL,
  `Observaciones` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;




CREATE TABLE `listasolicitantes` (
`Solicitante` varchar(50)
);

CREATE TABLE `minimos` (
`Clave` varchar(9)
,`Nombre` varchar(255)
,`Cantidad` decimal(11,0)
);



CREATE TABLE `min_max` (
  `Clave` varchar(9) NOT NULL,
  `Max` int(11) DEFAULT NULL,
  `Min` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;





CREATE TABLE `usuarios` (
  `ID` int(11) NOT NULL,
  `Usuario` varchar(25) NOT NULL,
  `Nombre` varchar(50) DEFAULT NULL,
  `ApellidoP` varchar(25) DEFAULT NULL,
  `ApellidoM` varchar(25) DEFAULT NULL,
  `Telefono` varchar(10) DEFAULT NULL,
  `NivelAutoridad` int(1) NOT NULL,
  `Contrasena` varchar(255) NOT NULL,
  `IMG` longblob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;




CREATE TABLE `vales` (
  `IDFolio` int(10) NOT NULL,
  `Folio` int(11) NOT NULL,
  `Clave` varchar(9) NOT NULL,
  `Nombre` varchar(255) NOT NULL,
  `Medida` varchar(20) NOT NULL,
  `Motivo` varchar(50) DEFAULT NULL,
  `Almacenista` varchar(50) NOT NULL,
  `Solicitante` varchar(50) NOT NULL,
  `Salida` int(3) NOT NULL,
  `Fecha` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;


DROP TABLE IF EXISTS `listasolicitantes`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `listasolicitantes`  AS SELECT DISTINCT `vales`.`Solicitante` AS `Solicitante` FROM `vales` ;


DROP TABLE IF EXISTS `minimos`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `minimos`  AS SELECT `g`.`Clave` AS `Clave`, `g`.`Nombre` AS `Nombre`, `g`.`Cantidad` AS `Cantidad` FROM (`gastos` `g` join `min_max` `m` on(`g`.`Clave` = `m`.`Clave`)) WHERE `g`.`Cantidad` <= `m`.`Min` ;


ALTER TABLE `gastos`
  ADD PRIMARY KEY (`ID`);

ALTER TABLE `historialmovimientos`
  ADD PRIMARY KEY (`ID`);

ALTER TABLE `min_max`
  ADD PRIMARY KEY (`Clave`);


ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`ID`);

ALTER TABLE `vales`
  ADD PRIMARY KEY (`IDFolio`);


ALTER TABLE `gastos`
  MODIFY `ID` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=851;


ALTER TABLE `historialmovimientos`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

ALTER TABLE `usuarios`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

ALTER TABLE `vales`
  MODIFY `IDFolio` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;
