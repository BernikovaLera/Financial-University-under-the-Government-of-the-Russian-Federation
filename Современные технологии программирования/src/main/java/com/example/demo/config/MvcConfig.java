package com.example.demo.config;


import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.ViewControllerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class MvcConfig implements WebMvcConfigurer {

    public void addViewControllers(ViewControllerRegistry registry) {
        registry.addViewController("/").setViewName("index"); // Главная страница
        registry.addViewController("/login").setViewName("login"); // Страница входа
        registry.addViewController("/aboutTheAuthor").setViewName("aboutTheAuthor"); // Страница об авторе
        registry.addViewController("/user/home").setViewName("userRequest"); // Страница пользователя
        registry.addViewController("/admin/home").setViewName("adminRequest"); // Страница администратора
    }
}