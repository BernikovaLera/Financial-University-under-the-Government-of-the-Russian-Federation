package com.example.demo.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.provisioning.InMemoryUserDetailsManager;
import org.springframework.security.web.SecurityFilterChain;

@Configuration
@EnableWebSecurity
public class WebSecurityConfig {
    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http
                .authorizeHttpRequests((requests) -> requests
                        .requestMatchers("/", "/login").permitAll() // Разрешить доступ к главной и странице входа
                        .requestMatchers("/admin/**").hasRole("ADMIN") // Доступ для администратора
                        .requestMatchers("/user/**").hasRole("USER") // Доступ для пользователя
                        .anyRequest().authenticated() // Все остальные запросы требуют аутентификации
                )
                .formLogin((form) -> form
                        .loginPage("/login")
                        .failureUrl("/login?error=true") // URL для перенаправления при ошибке входа// Страница входа
                        .successHandler((request, response, authentication) -> {
                            if (authentication.getAuthorities().stream()
                                    .anyMatch(grantedAuthority -> grantedAuthority.getAuthority().equals("ADMIN"))) {
                                response.sendRedirect("/admin/home");
                            } else {
                                response.sendRedirect("/user/home");
                            }
                        })
                        .permitAll()
                )
                .logout((logout) -> logout.permitAll()); // Разрешить выход

        return http.build();
    }

    @Bean
    public UserDetailsService userDetailsService() throws Exception {
        User.UserBuilder users = User.withDefaultPasswordEncoder();
        UserDetails user = users
                .username("user")
                .password("12345")
                .roles("USER")
                .build();
        UserDetails admin = users
                .username("admin")
                .password("qwert")
                .roles("ADMIN")
                .build();

        return new InMemoryUserDetailsManager(user, admin);
    }
}
