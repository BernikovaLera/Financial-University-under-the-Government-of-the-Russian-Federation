package com.example.demo.controller;

import com.example.demo.domain.Request;
import com.example.demo.service.RequestService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

import java.time.LocalDateTime;
import java.time.ZoneId;
import java.util.List;

@Controller
@RequestMapping("/admin")
public class AdminReqController {
    @Autowired
    private RequestService service;

    @RequestMapping("/home")
    public String homePage(Model model, @Param("keyword") String keyword) {
        List<Request> listRequest = service.listAll(keyword);
        model.addAttribute("listRequest", listRequest);
        model.addAttribute("keyword", keyword);
        return "adminRequest";
    }
    @RequestMapping("/create")
    public String newForm(Model model) {
        var request = new Request();
        model.addAttribute("request", request);
        return "createRequest";
    }

    @RequestMapping(value = "/save", method = RequestMethod.POST)
    public String saveForm(@ModelAttribute("request") Request request) {
        // Установка статуса по умолчанию
        request.setStatus("Новая");
        // Установка текущего времени создания и изменения в зависимости от часового пояса
        LocalDateTime now = LocalDateTime.now(ZoneId.systemDefault());
        request.setCreatedDate(now);
        request.setModifiedDate(now);
        service.save(request);
        return "redirect:/home";
    }

    @RequestMapping("/edit/{id}")
    public ModelAndView editForm(@PathVariable(name = "id") Long id) {
        ModelAndView mav = new ModelAndView("editRequest");
        var request = service.get(id);
        mav.addObject("request", request);
        return mav;
    }
    @RequestMapping("/delete/{id}")
    public String deleteForm(@PathVariable(name = "id") Long id) {
        service.delete(id);
        return "redirect:/home";
    }
}
