-- phpMyAdmin SQL Dump
-- version 5.2.2
-- https://www.phpmyadmin.net/
--
-- Хост: localhost:3306
-- Время создания: Май 18 2026 г., 09:14
-- Версия сервера: 10.11.16-MariaDB-cll-lve
-- Версия PHP: 8.4.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `itvtop_vpn_new`
--

-- --------------------------------------------------------

--
-- Структура таблицы `partners_bots`
--

CREATE TABLE `partners_bots` (
  `id` int(11) NOT NULL,
  `partner_name` varchar(255) DEFAULT NULL,
  `bot_token` varchar(150) NOT NULL,
  `bot_username` varchar(100) NOT NULL,
  `webhook_hash` varchar(64) NOT NULL,
  `brand_name` varchar(100) DEFAULT 'VPN Service',
  `support_contact` varchar(100) DEFAULT '@admin',
  `admin_id` varchar(64) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `partners_bots`
--

INSERT INTO `partners_bots` (`id`, `partner_name`, `bot_token`, `bot_username`, `webhook_hash`, `brand_name`, `support_contact`, `admin_id`, `created_at`) VALUES
(3, 'usepetro (@usepetro)', '7959047813:AAFDoOyyVI_fHL4FWGv2wvAEnDN3OaU-L3E', '@MessiVPN_bot', '6661531d1bf080075c46f3bad40dc999', 'Messi VPN', '@usepetro', '6071971939', '2026-05-12 05:48:40');

-- --------------------------------------------------------

--
-- Структура таблицы `vpn_payments`
--

CREATE TABLE `vpn_payments` (
  `id` int(11) NOT NULL,
  `m_id` varchar(255) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `payment_time` datetime DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `vpn_users`
--

CREATE TABLE `vpn_users` (
  `id` int(11) NOT NULL,
  `user_id` varchar(50) NOT NULL,
  `username` varchar(255) DEFAULT NULL,
  `balance` decimal(10,2) DEFAULT 0.00,
  `subscription_until` datetime DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `referrer_id` bigint(20) DEFAULT NULL,
  `ref_earnings` decimal(10,2) DEFAULT 0.00,
  `welcome_bonus_given` tinyint(1) DEFAULT 0,
  `lang` varchar(2) DEFAULT 'ru',
  `trial_used` tinyint(1) DEFAULT 0,
  `vpn_key` text DEFAULT NULL,
  `ip_limit` int(11) DEFAULT 3,
  `short_url` varchar(255) DEFAULT NULL,
  `last_message_id` bigint(20) DEFAULT NULL,
  `reminder_sent` tinyint(1) DEFAULT 0,
  `admin_mode` varchar(50) DEFAULT NULL,
  `origin_bot_token` varchar(100) DEFAULT NULL,
  `total_paid` decimal(10,2) DEFAULT 0.00,
  `language_code` varchar(5) DEFAULT 'en'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `vpn_users`
--

INSERT INTO `vpn_users` (`id`, `user_id`, `username`, `balance`, `subscription_until`, `created_at`, `referrer_id`, `ref_earnings`, `welcome_bonus_given`, `lang`, `trial_used`, `vpn_key`, `ip_limit`, `short_url`, `last_message_id`, `reminder_sent`, `admin_mode`, `origin_bot_token`, `total_paid`, `language_code`) VALUES
(6, '6071971939', 'usepetro', 0.00, '2026-05-15 20:37:05', '2026-05-14 17:36:57', NULL, 0.00, 0, 'ru', 1, 'vless://1e2c3f1c-6b11-427d-b773-eb143935478f@130.61.252.216:443?type=tcp&encryption=none&security=reality&pbk=lteN47eDj5VnDY8zlIpP6YtM2JF9X2BXGzBGFmOXKRI&fp=chrome&sni=google.com&sid=5d0965#Messi VPN', 1, 'https://is.gd/WPZX4t', 121, 0, NULL, '7959047813:AAFDoOyyVI_fHL4FWGv2wvAEnDN3OaU-L3E', 0.00, 'en'),
(7, '7887718763', 'userme1975', 0.00, '2026-05-15 22:52:37', '2026-05-14 19:52:25', NULL, 0.00, 0, 'ru', 1, 'vless://f7439c9f-ef34-436f-9e6a-14714bef03bf@130.61.252.216:443?type=tcp&encryption=none&security=reality&pbk=lteN47eDj5VnDY8zlIpP6YtM2JF9X2BXGzBGFmOXKRI&fp=chrome&sni=google.com&sid=5d0965#Messi VPN', 1, 'https://is.gd/bFhi9t', 59, 0, NULL, '7959047813:AAFDoOyyVI_fHL4FWGv2wvAEnDN3OaU-L3E', 0.00, 'en'),
(8, '7522142669', 'Lizazelentsova', 5.00, '2026-12-13 12:17:47', '2026-05-16 09:17:39', NULL, 0.00, 0, 'ru', 1, 'vless://44ebcee4-4bcc-49ba-bc56-b16e87462f86@130.61.252.216:443?type=tcp&encryption=none&security=reality&pbk=lteN47eDj5VnDY8zlIpP6YtM2JF9X2BXGzBGFmOXKRI&fp=chrome&sni=google.com&sid=5d0965#Messi VPN', 1, 'https://is.gd/FKMGdE', 62, 0, NULL, '7959047813:AAFDoOyyVI_fHL4FWGv2wvAEnDN3OaU-L3E', 0.00, 'en'),
(9, '6853699546', 'Rovsen100', 0.00, '2026-05-19 00:50:41', '2026-05-17 21:50:23', NULL, 0.00, 0, 'ru', 1, 'vless://6c55dd3d-ed11-499c-a959-e3f8fa8736bd@130.61.252.216:443?type=tcp&encryption=none&security=reality&pbk=lteN47eDj5VnDY8zlIpP6YtM2JF9X2BXGzBGFmOXKRI&fp=chrome&sni=google.com&sid=5d0965#Messi VPN', 1, 'https://i-tv.top/vpn_new/handler.php?hash=6661531d1bf080075c46f3bad40dc999&sub=6853699546', 120, 0, NULL, '7959047813:AAFDoOyyVI_fHL4FWGv2wvAEnDN3OaU-L3E', 0.00, 'en');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `partners_bots`
--
ALTER TABLE `partners_bots`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `webhook_hash` (`webhook_hash`);

--
-- Индексы таблицы `vpn_payments`
--
ALTER TABLE `vpn_payments`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `m_id` (`m_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Индексы таблицы `vpn_users`
--
ALTER TABLE `vpn_users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`),
  ADD KEY `origin_bot_token` (`origin_bot_token`),
  ADD KEY `origin_bot_token_2` (`origin_bot_token`),
  ADD KEY `origin_bot_token_3` (`origin_bot_token`),
  ADD KEY `origin_bot_token_4` (`origin_bot_token`),
  ADD KEY `origin_bot_token_5` (`origin_bot_token`),
  ADD KEY `origin_bot_token_6` (`origin_bot_token`),
  ADD KEY `origin_bot_token_7` (`origin_bot_token`),
  ADD KEY `origin_bot_token_8` (`origin_bot_token`),
  ADD KEY `origin_bot_token_9` (`origin_bot_token`),
  ADD KEY `origin_bot_token_10` (`origin_bot_token`),
  ADD KEY `origin_bot_token_11` (`origin_bot_token`),
  ADD KEY `origin_bot_token_12` (`origin_bot_token`),
  ADD KEY `origin_bot_token_13` (`origin_bot_token`),
  ADD KEY `origin_bot_token_14` (`origin_bot_token`),
  ADD KEY `origin_bot_token_15` (`origin_bot_token`),
  ADD KEY `origin_bot_token_16` (`origin_bot_token`),
  ADD KEY `origin_bot_token_17` (`origin_bot_token`),
  ADD KEY `origin_bot_token_18` (`origin_bot_token`),
  ADD KEY `origin_bot_token_19` (`origin_bot_token`),
  ADD KEY `origin_bot_token_20` (`origin_bot_token`),
  ADD KEY `origin_bot_token_21` (`origin_bot_token`),
  ADD KEY `origin_bot_token_22` (`origin_bot_token`),
  ADD KEY `origin_bot_token_23` (`origin_bot_token`),
  ADD KEY `origin_bot_token_24` (`origin_bot_token`),
  ADD KEY `origin_bot_token_25` (`origin_bot_token`),
  ADD KEY `origin_bot_token_26` (`origin_bot_token`),
  ADD KEY `origin_bot_token_27` (`origin_bot_token`),
  ADD KEY `origin_bot_token_28` (`origin_bot_token`),
  ADD KEY `origin_bot_token_29` (`origin_bot_token`),
  ADD KEY `origin_bot_token_30` (`origin_bot_token`),
  ADD KEY `origin_bot_token_31` (`origin_bot_token`),
  ADD KEY `origin_bot_token_32` (`origin_bot_token`),
  ADD KEY `origin_bot_token_33` (`origin_bot_token`),
  ADD KEY `origin_bot_token_34` (`origin_bot_token`),
  ADD KEY `origin_bot_token_35` (`origin_bot_token`),
  ADD KEY `origin_bot_token_36` (`origin_bot_token`),
  ADD KEY `origin_bot_token_37` (`origin_bot_token`),
  ADD KEY `origin_bot_token_38` (`origin_bot_token`),
  ADD KEY `origin_bot_token_39` (`origin_bot_token`),
  ADD KEY `origin_bot_token_40` (`origin_bot_token`),
  ADD KEY `origin_bot_token_41` (`origin_bot_token`),
  ADD KEY `origin_bot_token_42` (`origin_bot_token`),
  ADD KEY `origin_bot_token_43` (`origin_bot_token`),
  ADD KEY `origin_bot_token_44` (`origin_bot_token`),
  ADD KEY `origin_bot_token_45` (`origin_bot_token`),
  ADD KEY `origin_bot_token_46` (`origin_bot_token`),
  ADD KEY `origin_bot_token_47` (`origin_bot_token`),
  ADD KEY `origin_bot_token_48` (`origin_bot_token`),
  ADD KEY `origin_bot_token_49` (`origin_bot_token`),
  ADD KEY `origin_bot_token_50` (`origin_bot_token`),
  ADD KEY `origin_bot_token_51` (`origin_bot_token`),
  ADD KEY `origin_bot_token_52` (`origin_bot_token`),
  ADD KEY `origin_bot_token_53` (`origin_bot_token`),
  ADD KEY `origin_bot_token_54` (`origin_bot_token`),
  ADD KEY `origin_bot_token_55` (`origin_bot_token`),
  ADD KEY `origin_bot_token_56` (`origin_bot_token`),
  ADD KEY `origin_bot_token_57` (`origin_bot_token`),
  ADD KEY `origin_bot_token_58` (`origin_bot_token`),
  ADD KEY `origin_bot_token_59` (`origin_bot_token`),
  ADD KEY `origin_bot_token_60` (`origin_bot_token`),
  ADD KEY `origin_bot_token_61` (`origin_bot_token`),
  ADD KEY `origin_bot_token_62` (`origin_bot_token`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `partners_bots`
--
ALTER TABLE `partners_bots`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `vpn_payments`
--
ALTER TABLE `vpn_payments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `vpn_users`
--
ALTER TABLE `vpn_users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
