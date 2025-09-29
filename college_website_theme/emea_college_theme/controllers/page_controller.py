from odoo import http
from odoo.http import request


class PageController(http.Controller):

    @http.route(['/Home/IQAC/Best Practices/1986'], type='http', auth='public', website=True)
    def custom_iqac_best_practices(self, **kwargs):
        return request.render('emea_college_theme.best_practices_emea_college_template', {

        })

    @http.route(['/Home/IQAC/Minutes _ ATR/174'], type='http', auth='public', website=True)
    def custom_iqac_minutes_atr(self, **kwargs):
        return request.render('emea_college_theme.minutes_atr_template', {

        })

    @http.route(['/Home/IQAC/Annual Reports/1987'], type='http', auth='public', website=True)
    def custom_iqac_annual_report(self, **kwargs):
        return request.render('emea_college_theme.annual_report_template', {

        })

    @http.route(['/Home/IQAC/Students Satisfaction Survey/1985'], type='http', auth='public', website=True)
    def custom_iqac_students_satisfaction_survey(self, **kwargs):
        return request.render('emea_college_theme.students_satisfaction_survey_template', {

        })

    @http.route(['/Home/IQAC/Activities/179'], type='http', auth='public', website=True)
    def custom_iqac_activities(self, **kwargs):
        return request.render('emea_college_theme.iqac_activities_template', {

        })

    @http.route(['/Home/IQAC/Feedback/1731'], type='http', auth='public', website=True)
    def custom_iqac_feedback_report(self, **kwargs):
        return request.render('emea_college_theme.feedback_report_template', {

        })

    @http.route(['/Home/IQAC/Feedback/1732'], type='http', auth='public', website=True)
    def custom_iqac_feedback_atr(self, **kwargs):
        return request.render('emea_college_theme.feedback_atr_template', {

        })

    @http.route(['/Home/IQAC/Gender Equity/2172'], type='http', auth='public', website=True)
    def custom_iqac_gender_equity(self, **kwargs):
        return request.render('emea_college_theme.gender_equity_template', {

        })

    @http.route(['/Home/IQAC/Mandatory Disclosure/1664'], type='http', auth='public', website=True)
    def custom_iqac_mandatory_disclosure(self, **kwargs):
        return request.render('emea_college_theme.mandatory_disclosure_template', {

        })

    @http.route(['/Home/IQAC/Composition/172'], type='http', auth='public', website=True)
    def custom_iqac_composition_iqac(self, **kwargs):
        return request.render('emea_college_theme.composition_iqac_template', {

        })

    @http.route(['/Home/Academics/AcademicCalendar'], type='http', auth='public', website=True)
    def custom_iqac_academic_calendar(self, **kwargs):
        return request.render('emea_college_theme.academic_calendar_template', {

        })

    @http.route(['/Home/IQAC/AQAR/173'], type='http', auth='public', website=True)
    def custom_iqac_aqar_page(self, **kwargs):
        return request.render('emea_college_theme.aqar_page_template', {

        })
