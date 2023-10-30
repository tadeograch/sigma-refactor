-- Date: 2023-10-10

DROP DATABASE IF EXISTS sigma;
CREATE DATABASE sigma;
USE sigma;

CREATE TABLE symbols (
    id INT NOT NULL AUTO_INCREMENT,
    symbol VARCHAR(10) NOT NULL,
    PRIMARY KEY (id)
);

-- Insert cryptocurrencies
INSERT INTO symbols (symbol) VALUE ("BTC-USD");
INSERT INTO symbols (symbol) VALUE ("ETH-USD");
INSERT INTO symbols (symbol) VALUE ("USDT-USD");
INSERT INTO symbols (symbol) VALUE ("BNB-USD");
INSERT INTO symbols (symbol) VALUE ("XRP-USD");
INSERT INTO symbols (symbol) VALUE ("USDC-USD");
INSERT INTO symbols (symbol) VALUE ("STETH-USD");
INSERT INTO symbols (symbol) VALUE ("SOL-USD");
INSERT INTO symbols (symbol) VALUE ("ADA-USD");
INSERT INTO symbols (symbol) VALUE ("WTRX-USD");
