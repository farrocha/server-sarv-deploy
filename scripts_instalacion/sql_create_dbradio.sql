

CREATE TABLE `tbl_programacion` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `IDRegistro` bigint(20) unsigned DEFAULT NULL,
  `IDPais` int(11) DEFAULT NULL,
  `FechaHora` datetime DEFAULT NULL,
  `IDMedio` int(11) DEFAULT NULL,
  `Huellas` int(11) DEFAULT NULL,
  `Stamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `Segundo` int(11) DEFAULT NULL,
  `Revision` int(11) NOT NULL DEFAULT '0',
  `Creacion` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`),
  KEY `PK_IDRegistro` (`IDRegistro`),
  KEY `PK_Revision` (`Revision`),
  KEY `PK_Pais_Fecha` (`IDPais`,`FechaHora`,`IDMedio`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;



CREATE TABLE `tbl_hash_versiones` (
  `ID` bigint(20) NOT NULL AUTO_INCREMENT,
  `IDVersion` int(11) NOT NULL,
  `IDPais` int(11) NOT NULL,
  `Offset` int(11) NOT NULL,
  `Vigente` int(11) NOT NULL DEFAULT '1',
  `hash` binary(10) NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `PK_Huellas` (`IDPais`,`Vigente`,`hash`),
  KEY `PK_Version_Huellas` (`IDVersion`,`hash`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;



CREATE TABLE `tbl_hash_programacion` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `IDRegistro` bigint(20) unsigned DEFAULT NULL,
  `IDPais` int(11) DEFAULT NULL,
  `FechaHora` datetime DEFAULT NULL,
  `IDMedio` int(11) DEFAULT NULL,
  `Segundo` int(11) DEFAULT NULL,
  `hash` binary(10) DEFAULT NULL,
  `offset` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `PK_IDPais_Fecha_IDMedio` (`IDPais`,`FechaHora`,`IDMedio`),
  KEY `PK_IDRegistro` (`IDRegistro`,`Segundo`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;


CREATE TABLE `tbl_versiones` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `IDVersion` int(11) DEFAULT NULL,
  `Huellas` int(11) DEFAULT NULL,
  `Duracion` int(11) DEFAULT NULL,
  `IDPais` int(11) DEFAULT NULL,
  `Stamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2946 DEFAULT CHARSET=latin1;

CREATE TABLE `tbl_log` (
  `IDLog` bigint(20) NOT NULL AUTO_INCREMENT,
  `Stamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `Paso` int(11) DEFAULT NULL,
  `Mensaje` varchar(345) DEFAULT NULL,
  `IDComputadora` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`IDLog`),
  KEY `PK_Paso` (`Paso`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;






