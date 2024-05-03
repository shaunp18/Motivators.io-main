import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tempfile
import os
from textwrap import wrap
import numpy as np
import random
from reportlab.lib import colors
            
def create_radar_chart(categories, values, filename):
    N = len(categories)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    values += values[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color='blue', alpha=0.25)
    ax.plot(angles, values, color='blue', linewidth=2)
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)

    plt.savefig(filename, bbox_inches='tight')


def generate_report(responses, report_messages):
    category_reports = {}
    for category, questions in responses.items():
        report = ""
        for question, rating in questions.items():
            try:
                report += f"{report_messages[category][question][rating]}\n"
            except KeyError as e:
                report += f"Error: Missing report message for '{question}' with rating {rating}. KeyError: {e}\n"
        category_reports[category] = report
    return category_reports
def get_user_input(question):
    # For testing purposes, automatically generate a random response
    response = random.randint(0, 5)
    return response
def add_motivators_to_pdf(motivators, title, y_pos, category_reports, canvas_obj):
    c = canvas_obj
    c.drawString(50, y_pos, title)
    y_pos -= 20

    for category, rating in motivators:
        if y_pos < 50:  # Check if near the bottom of the page
            c.showPage()  # Create a new page
            y_pos = 750   # Reset y_position for the new page

        c.drawString(50, y_pos, f"{category}: {rating}/100")
        y_pos -= 20

        # Retrieve and add the category report
        category_report = category_reports.get(category, "No report available.")
        wrapped_lines = wrap(category_report, width=80)
        for line in wrapped_lines:
            if y_pos < 50:  # Check if near the bottom of the page within the loop
                c.showPage()
                y_pos = 750

            c.drawString(50, y_pos, line)
            y_pos -= 14  # Adjust line spacing as needed

        y_pos -= 20  # Extra space before the next category

    return y_pos
def main():
    categories = {
    "Benefits and Wellness": [
        "A company that invests in employee recognition programs",
        "A generous vacation policy",
        "Access to a competitive health plan",
        "Access to a competitive retirement plan",
        "Access to employee wellness programs"
    ],
    "Building and Innovating": [
        "A company with a reputation for being innovative",
        "A company that consistently invests in Research and Development",
        "Working with emerging technologies in my job",
        "Brainstorming new ideas at work",
        "A company that invests in continuous improvement",
        "A company that encourages creative solutions"
    ],
    "Career Growth and Development": [
        "A company that frequently promotes employees into new jobs",
        "Access to a learning management system to support my career development",
        "Access to mentoring programs",
        "A job with a high likelihood of career advancement",
        "Access to external learning and development opportunities such as courses, conferences, etc.",
        "Learning new skills on the job"
    ],
    "Compensation": [
        "Receiving a total compensation package above the market average for my role",
        "Receiving a financial bonus if I meet my personal objectives",
        "A base salary above the market average for my role",
        "Receiving a financial bonus if my company meets its objectives",
        "A company that provides transparency into their salary ranges"
    ],
    "Culture and Values": [
        "A company that makes a consistent effort to improve the culture",
        "Working on projects that align with my personal values",
        "A company that makes business decisions based on culture and value alignment",
        "Consistently high scores for 'company culture' on employee surveys",
        "A company that only hires employees who demonstrate the desired values"
    ],
    "Executive Leadership": [
        "An executive team that holds themselves accountable",
        "Executive leadership that is accessible to employees",
        "Executive leadership that is transparent about business decisions",
        "Executive leadership with high approval ratings from employees",
        "An executive team that drives the organizational strategy"
    ],
    "Flexible Work": [
        "A job where my performance matters more than my total hours worked",
        "A company that offers a shorter workweek",
        "The option to permanently work remotely",
        "The opportunity to work from anywhere",
        "A company that supports me in balancing my work and personal responsibilities",
        "Flexible start and end times at work"
    ],
    "Inclusion and Social Connection": [
        "A company that seeks out partnerships with underrepresented communities",
        "A company that has a positive impact on my community",
        "Consistent investment in Diversity and Inclusion programs",
        "A company that encourages you to share your opinions at work",
        "Opportunities for social connection at work",
        "A company that invests in Corporate Social Responsibility programs"
    ],
    "Job Security and Stability": [
        "A company that prioritizes stability over rapid growth",
        "A job that is unlikely to be automated in the foreseeable future",
        "Knowing I could have a job with the same company for the rest of my working years",
        "An industry that can withstand an economic downturn",
        "A job with a consistent workload"
    ],
    "Manager Relationship": [
        "A manager who empowers me to make decisions on my own",
        "A manager who provides performance feedback to me",
        "A manager who provides recognition for my accomplishments",
        "A manager who supports my career development",
        "A manager who wants to get to know me as a person, not just an employee",
        "A manager who provides stretch opportunities to learn new skills"
    ],
    "Meaningful Work": [
        "A job that has a positive impact on the lives of others",
        "A company with an inspiring mission and purpose",
        "A company whose products have a positive impact on the world",
        "A company that is committed to environmental sustainability",
        "A job that provides meaning and purpose in my life"
    ],
    "Personal Impact": [
        "Having important responsibilities in my job",
        "Mentoring others at work",
        "Work that directly impacts customers",
        "Feeling a sense of accomplishment in my job",
        "Work that directly impacts the success of the company",
        "Leaving a legacy behind after I've left the company"
    ]
}


    report_messages = {
         "Benefits and Wellness": {
        "A company that invests in employee recognition programs": {
            0: "Employee recognition isn't a priority for you, suggesting you're self-reliant and internally motivated.",
            1: "You find some value in employee recognition, but it's not a major factor in your job satisfaction.",
            2: "You appreciate employee recognition to a moderate extent, balancing it with other aspects of your career.",
            3: "Employee recognition is quite important to you, which helps maintain your motivation and morale.",
            4: "You highly value recognition in the workplace, seeing it as crucial to your job satisfaction and motivation.",
            5: "You consider strong employee recognition programs extremely important, reflecting its significant impact on your workplace happiness and productivity."
        },
        "A generous vacation policy": {
            0: "You don't consider a generous vacation policy important, suggesting other aspects of work are more significant to you.",
            1: "You see some value in a generous vacation policy, but it's not a major factor for your job satisfaction.",
            2: "A generous vacation policy is moderately important to you, balancing it with other factors in your career.",
            3: "You find a generous vacation policy quite important, indicating you value work-life balance.",
            4: "You highly value a generous vacation policy, showing it's a key factor in your job satisfaction.",
            5: "A generous vacation policy is extremely important to you, suggesting you place a high priority on work-life balance and personal time."
        },
        "Access to a competitive health plan": {
            0: "You don't prioritize access to a competitive health plan, indicating other factors are more significant in your job choice.",
            1: "You find some slight importance in having a competitive health plan.",
            2: "You moderately value access to a competitive health plan, considering it a nice benefit.",
            3: "A competitive health plan is quite important to you, reflecting your concern for health benefits in your job.",
            4: "You place high importance on access to a competitive health plan, indicating it's a significant factor in your job satisfaction.",
            5: "You regard access to a competitive health plan as extremely important, showing you highly prioritize health benefits in your career decisions."
        },
        "Access to a competitive retirement plan": {
            0: "You don't prioritize access to a competitive retirement plan, indicating you have other priorities.",
            1: "You find some importance in a competitive retirement plan, but it's not a major consideration for you.",
            2: "You moderately value access to a competitive retirement plan, balancing it with other job aspects.",
            3: "Access to a competitive retirement plan is quite important to you, reflecting your focus on long-term financial stability.",
            4: "You place high importance on a competitive retirement plan, indicating it's a significant factor in your career planning.",
            5: "You view access to a competitive retirement plan as extremely important, showing a strong preference for secure and beneficial long-term financial planning."
        },
        "Access to employee wellness programs": {
            0: "You don't mind if a company invests in wellness programs, indicating other factors are more significant to you.",
            1: "You consider wellness programs as slightly important, suggesting you have other priorities.",
            2: "You moderately value wellness programs, balancing them with other factors in your career choice.",
            3: "You find wellness programs quite important, reflecting your awareness of well-being at work.",
            4: "You highly value wellness programs, indicating they are a key factor in your job satisfaction.",
            5: "You place maximum importance on wellness programs, showing a strong preference for supportive work environments."
        }
    }, 
        "Building and Innovating": {
        "A company with a reputation for being innovative": {
            0: "A company's reputation for innovation is not a significant factor for you, indicating other aspects of a job hold more value.",
            1: "You see some importance in a company's reputation for being innovative but it's not a major factor in your career choice.",
            2: "You moderately value a company's reputation for innovation, considering it a beneficial but not essential aspect of your work environment.",
            3: "A company known for its innovation is quite important to you, reflecting your appreciation for forward-thinking and creative work cultures.",
            4: "You highly value a company's reputation for innovation, indicating it's a significant factor in your job satisfaction and choice.",
            5: "A company's innovative reputation is extremely important to you, showing a strong preference for environments that foster creativity and leading-edge thinking."
        },
        "A company that consistently invests in Research and Development": {
            0: "Consistent investment in Research and Development is not a priority for you, suggesting other factors are more significant in your job choice.",
            1: "You find some value in a company's commitment to R&D, but it's not a major deciding factor for you.",
            2: "You moderately value a company that invests in R&D, seeing it as an important component of an innovative and evolving organization.",
            3: "Consistent investment in R&D is quite important to you, reflecting your preference for companies that prioritize innovation and advancement.",
            4: "You highly value a company's continuous investment in R&D, considering it crucial for staying at the forefront of industry developments.",
            5: "Extremely committed investment in R&D is very important to you, indicating a strong desire to be part of an organization that leads in innovation and technological advancements."
        },
        "Working with emerging technologies in my job": {
            0: "Working with emerging technologies is not a key priority for you, suggesting comfort with existing or traditional technologies.",
            1: "You see some importance in working with emerging technologies but do not consider it a central aspect of your job.",
            2: "You moderately value the opportunity to work with emerging technologies, considering it advantageous for your skillset and career growth.",
            3: "The chance to work with emerging technologies is quite important to you, reflecting a desire to be involved in cutting-edge and innovative work.",
            4: "You highly value working with emerging technologies, seeing it as essential to your professional development and staying relevant in your field.",
            5: "Working with the latest and emerging technologies is extremely important to you, indicating a strong preference for being at the forefront of technological advancements."
        },
        "Brainstorming new ideas at work": {
            0: "Brainstorming new ideas at work is not a significant factor in your job satisfaction, suggesting other areas are more important to you.",
            1: "You find some value in brainstorming new ideas at work but it's not a major aspect of your job.",
            2: "You moderately value the opportunity to brainstorm new ideas, considering it beneficial for creativity and innovation in your role.",
            3: "Actively brainstorming new ideas at work is quite important to you, reflecting your interest in creativity and collaborative innovation.",
            4: "You highly value the chance to brainstorm new ideas, seeing it as critical to your job satisfaction and contribution to the company.",
            5: "Brainstorming and generating new ideas at work is extremely important to you, indicating a strong desire for a creative and dynamic work environment."
        },
        "A company that invests in continuous improvement": {
            0: "A company's investment in continuous improvement is not a key concern for you, suggesting satisfaction with maintaining the status quo.",
            1: "You see some importance in a company's commitment to continuous improvement but it's not a major factor in your job choice.",
            2: "You moderately value a company's focus on continuous improvement, considering it beneficial for long-term success and adaptability.",
            3: "A company's dedication to continuous improvement is quite important to you, reflecting your preference for progressive and evolving workplaces.",
            4: "You highly value a company's investment in continuous improvement, considering it crucial for staying competitive and innovative.",
            5: "Extremely committed to continuous improvement, it's very important to you, indicating a strong preference for working in environments that constantly seek to evolve and enhance."
        },
        "A company that encourages creative solutions": {
            0: "Encouraging creative solutions is not a significant factor for you, suggesting other aspects of work are more important.",
            1: "You find some value in a company that encourages creativity, but it's not a central factor in your job satisfaction.",
            2: "You moderately value a company that fosters creative solutions, considering it an important aspect of a dynamic work environment.",
            3: "A company that encourages creative solutions is quite important to you, reflecting your desire for innovation and out-of-the-box thinking in your work.",
            4: "You highly value a workplace that encourages creativity, seeing it as essential to your engagement and effectiveness in your role.",
            5: "Extremely encouraging of creative solutions, it's very important to you, indicating a strong preference for a workplace that values and fosters creativity and innovation."
        }
    },

        "Career Growth and Development": {
        "A company that frequently promotes employees into new jobs": {
            0: "Frequent internal promotions are not a priority for you, suggesting contentment with your current role or focus on external opportunities.",
            1: "You see some importance in internal promotions but do not consider them a major aspect of your career planning.",
            2: "You moderately value a company’s support for transfers and promotions, balancing it with other job aspects.",
            3: "Company support for internal career moves is quite important to you, reflecting your interest in varied experiences within the organization.",
            4: "You highly value a company that facilitates transfers and promotions, viewing it as essential for your career satisfaction.",
            5: "Employee transfers and promotions are extremely important to you, indicating a strong desire for career mobility and progression within the company."
        },
        "Access to a learning management system to support my career development": {
            0: "Access to a learning management system is not a significant concern for you, suggesting self-sufficiency or alternative learning methods.",
            1: "You find some value in having access to a learning management system, but it's not a major factor for your career growth.",
            2: "You moderately value access to a learning management system, considering it beneficial for your professional development.",
            3: "A learning management system is quite important to you, indicating a preference for structured and accessible learning resources.",
            4: "You highly value having access to a learning management system, viewing it as crucial for your continuous learning and career advancement.",
            5: "Extremely high importance is placed on access to a learning management system, showing a strong desire for comprehensive and organized learning support."
        },
        "Access to mentoring programs": {
            0: "Mentoring programs are not a priority for you, suggesting reliance on your own skills or other forms of professional development.",
            1: "You find some value in mentoring programs but prioritize other aspects of your career more.",
            2: "You moderately value mentoring programs, considering them beneficial but not critical for your growth.",
            3: "Mentoring programs are quite important to you, reflecting a commitment to guided professional development.",
            4: "You highly value mentoring opportunities, seeing them as integral to your career progression.",
            5: "Mentoring is extremely important to you, indicating a strong desire for continuous guidance and learning in your career."
        },
        "A job with a high likelihood of career advancement": {
            0: "Career advancement in your current job is not a priority, suggesting satisfaction with your current role or external aspirations.",
            1: "You find some importance in career advancement opportunities but focus more on other job aspects.",
            2: "You moderately value the likelihood of career advancement, considering it an important but not sole factor in your job satisfaction.",
            3: "A high likelihood of career advancement is quite important to you, reflecting ambition and a desire for growth.",
            4: "You highly value career advancement opportunities, seeing them as critical to your job choice and satisfaction.",
            5: "Career advancement is extremely important to you, indicating a strong focus on upward mobility in your career."
        },
        "Access to external learning and development opportunities such as courses, conferences, etc.": {
            0: "External learning opportunities are not a key consideration for you, suggesting other priorities or learning methods.",
            1: "You see some value in external learning opportunities but do not consider them essential for your career.",
            2: "You moderately value external learning and development opportunities, viewing them as beneficial additions to your career.",
            3: "Access to external courses and conferences is quite important to you, indicating a desire for broadening your knowledge and network.",
            4: "You highly value external learning opportunities, considering them integral to your professional development and networking.",
            5: "External learning and development opportunities are extremely important to you, indicating a high priority for external growth and exposure."
        },
        "Learning new skills on the job": {
            0: "Learning new skills at work is not a priority, suggesting reliance on your existing skill set or external learning.",
            1: "You find some value in on-the-job learning but prioritize other aspects of your job more.",
            2: "You moderately value learning new skills at work, considering it beneficial but not critical.",
            3: "On-the-job skill development is quite important to you, reflecting a commitment to continuous learning.",
            4: "You highly value learning new skills at work, seeing it as integral to your professional development.",
            5: "Learning new skills on the job is extremely important to you, indicating a strong desire for continual growth and adaptability in your role."
        }
    },
        "Compensation": {
        "Receiving a total compensation package above the market average for my role": {
            0: "A compensation package above market average is not a key factor for you, suggesting other aspects of the job are more significant.",
            1: "You find some importance in having a compensation package above market average, but it's not a major consideration.",
            2: "You moderately value a compensation package above the market average, balancing it with other job benefits.",
            3: "Having a total compensation package above market average is quite important to you, reflecting your focus on financial rewards.",
            4: "You highly value receiving a compensation package that exceeds market averages, indicating it's a significant factor in your career choices.",
            5: "Receiving a total compensation package well above the market average is extremely important to you, showing a strong preference for financial recognition of your skills and contributions."
        },
        "Receiving a financial bonus if I meet my personal objectives": {
            0: "Financial bonuses or commissions are not a priority for you, suggesting you are motivated by other job aspects.",
            1: "You see some value in receiving financial bonuses, but they're not a key driver for your performance.",
            2: "You moderately value financial bonuses or commissions, considering them a nice perk for meeting objectives.",
            3: "Receiving a bonus or commission for achieving personal objectives is quite important to you, reflecting a desire for performance-based financial rewards.",
            4: "You highly value financial bonuses or commissions, seeing them as essential motivators for exceeding your personal objectives.",
            5: "Financial rewards for meeting or exceeding personal objectives are extremely important to you, indicating a strong alignment of financial incentives with your performance goals."
        },
        "A base salary above the market average for my role": {
            0: "Having a base salary above the market average is not a priority, suggesting satisfaction with other job benefits or salary levels.",
            1: "You see some value in a higher-than-average base salary, but it's not a central factor in your job satisfaction.",
            2: "You moderately value a base salary above the market average, considering it an important but not sole factor in your compensation.",
            3: "A base salary above the market average is quite important to you, reflecting your focus on financial recognition for your skills.",
            4: "You highly value having a base salary above the market average, indicating it's a significant consideration in your career choices.",
            5: "Receiving a base salary well above the market average is extremely important to you, showing a strong emphasis on financial compensation in your career."
        },
        "Receiving a financial bonus if my company meets or exceeds its objectives": {
            0: "Company-wide financial bonuses are not a significant motivator for you, suggesting other factors drive your job satisfaction.",
            1: "You find some importance in receiving a company-wide bonus, but it's not a major factor in your job engagement.",
            2: "You moderately value receiving a financial bonus based on company performance, considering it a nice addition to your compensation.",
            3: "Receiving a bonus for company-wide achievements is quite important to you, reflecting your interest in the overall success of your organization.",
            4: "You highly value financial bonuses tied to company objectives, seeing them as crucial motivators for your engagement and performance.",
            5: "Company-wide financial bonuses are extremely important to you, indicating a strong alignment with the company's success and financial rewards."
        },
        "A company that provides transparency into their salary ranges": {
            0: "Transparency in salary ranges is not a significant concern for you, suggesting confidence in your current compensation or other priorities.",
            1: "You find some value in salary transparency but do not consider it a central aspect of your job decision.",
            2: "You moderately value transparency in salary ranges, seeing it as beneficial for fairness and informed decision-making.",
            3: "Salary range transparency is quite important to you, reflecting your preference for openness and fairness in compensation.",
            4: "You highly value a company that provides transparency into their salary ranges, considering it crucial for trust and equity in the workplace.",
            5: "Extremely high importance is placed on salary range transparency, indicating a strong preference for clear and open communication about compensation."
        }
    },
        "Culture and Values": {
        "A company that makes a consistent effort to improve the culture": {
            0: "Efforts to improve company culture are not a significant concern for you, indicating other priorities.",
            1: "You recognize some value in a company's effort to improve culture, but it's not a major factor in your job satisfaction.",
            2: "You moderately value a company's consistent effort to improve its culture, seeing it as an important aspect of the work environment.",
            3: "Consistent efforts to improve company culture are quite important to you, reflecting your preference for a dynamic and evolving work environment.",
            4: "You highly value a company that actively works on improving its culture, considering it crucial for your engagement and satisfaction.",
            5: "A company's ongoing effort to enhance its culture is extremely important to you, indicating a strong desire for a progressive and positive work environment."
        },
        "Working on projects that align with my personal values": {
            0: "Alignment of work projects with your personal values is not a key factor, suggesting other motivations in your career.",
            1: "You find some importance in working on projects that align with your values, but it's not a central factor for you.",
            2: "You moderately value working on projects aligned with your personal values, considering it beneficial to your job satisfaction.",
            3: "Working on projects that resonate with your personal values is quite important, reflecting a desire for meaningful and congruent work.",
            4: "You highly value alignment of your work with personal values, seeing it as essential to your motivation and fulfillment.",
            5: "Working on projects that deeply align with your personal values is extremely important to you, indicating a strong preference for work that reflects your personal ethos."
        },
        "A company that makes business decisions based on culture and value alignment": {
            0: "A company's alignment of business decisions with its culture and values is not a significant concern for you.",
            1: "You see some importance in a company aligning its business decisions with its culture and values, but it's not a major factor.",
            2: "You moderately value a company's effort to align business decisions with its culture and values, considering it an important aspect of its identity.",
            3: "You find it quite important that a company aligns its business decisions with its culture and values, reflecting your preference for congruence in organizational practices.",
            4: "You highly value a company that bases its business decisions on culture and value alignment, considering it crucial for authenticity and integrity.",
            5: "A company's alignment of business decisions with its culture and values is extremely important to you, showing a strong desire for consistent and value-driven practices."
        },
        "Consistently high scores for 'company culture' on employee surveys": {
            0: "High scores for company culture are not a priority for you, suggesting you prioritize other aspects of a job.",
            1: "You find some importance in consistently high scores for company culture, but it's not a central consideration for you.",
            2: "You moderately value high scores for company culture, seeing them as indicative of a positive work environment.",
            3: "Consistently high scores for company culture are quite important to you, reflecting a desire for a well-regarded and positive work environment.",
            4: "You highly value a company with consistently high scores for its culture, seeing it as a significant factor in your job choice.",
            5: "Consistently high scores for company culture are extremely important to you, indicating a strong preference for working in highly-regarded cultural environments."
        },
        "A company that only hires employees who demonstrate the desired values": {
            0: "A company's emphasis on hiring employees who align with its values is not a significant factor for you.",
            1: "You see some importance in a company hiring employees who align with its values, but it's not a major factor for your job satisfaction.",
            2: "You moderately value a company's focus on hiring employees who demonstrate its desired values, considering it beneficial to the work environment.",
            3: "You find it quite important that a company hires employees who align with its values, reflecting your preference for a value-driven work community.",
            4: "You highly value a company's commitment to hiring employees who embody its values, considering it crucial for maintaining a cohesive and positive culture.",
            5: "A company's focus on hiring employees who demonstrate its desired values is extremely important to you, indicating a strong desire for a values-aligned work community."
        }
    },
        "Executive Leadership": {
        "An executive team that holds themselves accountable": {
            0: "Self-accountability of the executive team is not a major factor for you, indicating other aspects of leadership are more important.",
            1: "You find some importance in executive accountability, but it's not a central factor in your view of company leadership.",
            2: "You moderately value an executive team that holds themselves accountable, considering it an important aspect of responsible leadership.",
            3: "Accountability within the executive team is quite important to you, reflecting your preference for transparent and responsible leadership.",
            4: "You highly value a self-accountable executive team, seeing it as essential for trust and integrity in the company's leadership.",
            5: "An executive team that holds themselves accountable is extremely important to you, indicating a strong desire for ethical and responsible leadership practices."
        },
        "Executive leadership that is accessible to employees": {
            0: "Accessible executive leadership is not a significant priority for you, suggesting other leadership qualities are more important.",
            1: "You recognize some value in having accessible leaders, but it's not a major factor in your job satisfaction.",
            2: "You moderately value accessible executive leadership, considering it beneficial for communication and organizational culture.",
            3: "Having accessible leadership is quite important to you, reflecting your preference for approachable and engaged executives.",
            4: "You highly value executive leadership that is accessible to employees, seeing it as crucial for effective communication and a positive work environment.",
            5: "Extremely accessible executive leadership is very important to you, indicating a strong preference for leaders who are actively involved and approachable."
        },
        "Executive leadership that is transparent about business decisions": {
            0: "Transparency in business decisions from executive leadership is not a key priority for you.",
            1: "You find some value in transparency about business decisions, but it's not a central factor in your view of effective leadership.",
            2: "You moderately value transparency in business decisions from executive leadership, considering it an important aspect of trust and integrity.",
            3: "Executive leadership that is transparent about business decisions is quite important to you, reflecting your preference for openness and clarity in company direction.",
            4: "You highly value transparency from executive leadership regarding business decisions, seeing it as essential to your confidence and alignment with the company.",
            5: "Extremely high transparency about business decisions from executive leadership is very important to you, indicating a strong desire for openness and honesty in corporate governance."
        },
        "Executive leadership with high approval ratings from employees": {
            0: "High approval ratings for executive leadership are not a significant factor for you, suggesting other aspects of leadership are more important.",
            1: "You see some importance in high approval ratings for executive leadership, but it's not a major factor in your job satisfaction.",
            2: "You moderately value high approval ratings for executive leadership, considering it indicative of effective and respected leadership.",
            3: "Executive leadership with high approval ratings is quite important to you, reflecting your preference for well-regarded and effective leaders.",
            4: "You highly value executive leadership with high approval ratings, viewing it as crucial for organizational trust and leadership effectiveness.",
            5: "Extremely high approval ratings for executive leadership are very important to you, indicating a strong preference for leaders who are highly respected and effective."
        },
        "An executive team that drives the organizational strategy": {
            0: "The role of the executive team in driving organizational strategy is not a major concern for you, suggesting other aspects of their role are more significant.",
            1: "You find some importance in an executive team that drives the company's strategy, but it's not a central factor in your job satisfaction.",
            2: "You moderately value an executive team that actively drives the organizational strategy, seeing it as beneficial for the company's direction and success.",
            3: "An executive team that leads the organizational strategy is quite important to you, reflecting your preference for proactive and strategic leadership.",
            4: "You highly value an executive team that is actively involved in driving the organizational strategy, considering it crucial for the company's growth and success.",
            5: "Extremely active involvement in driving the organizational strategy by the executive team is very important to you, indicating a strong preference for strategic and visionary leadership."
        }
    },
        "Flexible Work": {
        "A job where my performance matters more than my total hours worked": {
            0: "Prioritizing performance over total hours worked is not a significant factor for you, indicating comfort with traditional work metrics.",
            1: "You see some value in a performance-based work environment, but it's not a major aspect of your job satisfaction.",
            2: "You moderately value a job where performance matters more than hours, considering it a beneficial but not sole factor in your work life.",
            3: "A job that emphasizes performance over hours is quite important to you, reflecting your preference for efficiency and results-oriented work.",
            4: "You highly value a workplace that prioritizes performance over the number of hours worked, seeing it as crucial to your productivity and job satisfaction.",
            5: "Extremely high importance is placed on performance over total hours worked, indicating a strong desire for a results-focused work environment."
        },
        "A company that offers a shorter workweek": {
            0: "Having a shorter workweek is not a priority for you, suggesting other factors in a job are more significant.",
            1: "You find some value in the option of a shorter workweek, but it's not a central factor in your job choice.",
            2: "You moderately value the option of a shorter workweek, considering it beneficial for work-life balance but not essential.",
            3: "A shorter workweek is quite important to you, reflecting your desire for more personal time and work flexibility.",
            4: "You highly value the option of a shorter workweek, seeing it as essential to your work-life balance and overall well-being.",
            5: "Extremely high importance is placed on having a shorter workweek, indicating a strong preference for significant work flexibility and personal time."
        },
        "The option to permanently work remotely": {
            0: "Permanent remote work is not a significant factor in your job satisfaction, indicating a preference for traditional office settings or other priorities.",
            1: "You see some value in the option to work remotely, but it's not a major factor in your career decisions.",
            2: "You moderately value the option for permanent remote work, considering it a beneficial aspect of job flexibility.",
            3: "Having the option to work remotely on a permanent basis is quite important to you, reflecting your desire for location independence and flexibility.",
            4: "You highly value the ability to work remotely permanently, viewing it as crucial for your lifestyle and work preferences.",
            5: "Extremely high importance is placed on the option to work remotely permanently, indicating a strong preference for maximum location flexibility and autonomy."
        },
        "The opportunity to work from anywhere": {
            0: "The opportunity to work from anywhere is not a significant priority for you, suggesting satisfaction with fixed work locations or other aspects of work.",
            1: "You find some value in the ability to work from anywhere, but it's not a central factor in your job choice.",
            2: "You moderately value the opportunity to work from any location, considering it a beneficial aspect of job flexibility.",
            3: "Working from anywhere is quite important to you, reflecting your desire for geographical freedom and flexibility in your job.",
            4: "You highly value the opportunity to work from anywhere, seeing it as essential to your work satisfaction and lifestyle.",
            5: "Extremely high importance is placed on the ability to work from anywhere, indicating a strong preference for complete geographical independence and flexibility."
        },
        "A company that supports me in balancing my work and personal responsibilities": {
            0: "Support for balancing work and personal responsibilities is not a key factor for you, suggesting other aspects of a job are more significant.",
            1: "You find some value in a company that supports work-life balance, but it's not a major aspect of your job satisfaction.",
            2: "You moderately value a company that helps you balance work and personal responsibilities, considering it important for overall well-being.",
            3: "A company that supports balancing work and personal life is quite important to you, reflecting your focus on maintaining a healthy work-life equilibrium.",
            4: "You highly value a company that actively supports work-personal life balance, viewing it as critical to your productivity and personal well-being.",
            5: "Extremely high importance is placed on a company's support for balancing work and personal responsibilities, indicating a strong preference for a supportive and understanding work environment."
        },
        "Flexible start and end times at work": {
            0: "Flexible start and end times at work are not a significant priority for you, suggesting comfort with standard working hours or other priorities.",
            1: "You recognize some value in having flexible working hours, but it's not a major factor in your job satisfaction.",
            2: "You moderately value flexible start and end times, considering them beneficial for managing your schedule and work-life balance.",
            3: "Flexible working hours are quite important to you, reflecting your preference for autonomy and control over your work schedule.",
            4: "You highly value the ability to have flexible start and end times at work, seeing it as crucial to your overall job satisfaction and work-life balance.",
            5: "Extremely high importance is placed on flexible working hours, indicating a strong preference for control over your work schedule and better integration with personal life."
        }
    },
    "Inclusion and Social Connection": {
        "A company that seeks out partnerships with underrepresented communities": {
            0: "Partnerships with underrepresented communities are not a significant factor for you, indicating other priorities in your view of company values.",
            1: "You find some importance in company partnerships with underrepresented communities, but it's not a major factor in your job satisfaction.",
            2: "You moderately value a company's efforts to partner with underrepresented communities, seeing it as beneficial to diversity and inclusion.",
            3: "Such partnerships are quite important to you, reflecting your desire for a company that actively supports inclusivity and community engagement.",
            4: "You highly value a company's commitment to partnering with underrepresented communities, viewing it as crucial for corporate social responsibility.",
            5: "Extremely high importance is placed on a company's efforts to engage with underrepresented communities, indicating a strong preference for inclusive and socially responsible practices."
        },
        "A company that has a positive impact on my community": {
            0: "A company's impact on your community is not a key concern for you, suggesting other aspects of the company are more significant.",
            1: "You recognize some value in a company's positive impact on the community, but it's not a major factor in your job choice.",
            2: "You moderately value a company's positive impact on the community, considering it an important aspect of corporate responsibility.",
            3: "A company's contribution to the community is quite important to you, reflecting your preference for companies that are community-oriented and responsible.",
            4: "You highly value a company's positive impact on your community, seeing it as essential for your alignment with the company's values.",
            5: "Extremely high importance is placed on a company's positive impact on the community, indicating a strong desire to work for a company that is socially responsible and community-focused."
        },
        "Consistent investment in Diversity and Inclusion programs": {
            0: "Consistent investment in Diversity and Inclusion programs is not a significant priority for you, suggesting other aspects of the company are more important.",
            1: "You find some value in a company's commitment to Diversity and Inclusion, but it's not a central factor in your job satisfaction.",
            2: "You moderately value a company's consistent investment in Diversity and Inclusion programs, considering it beneficial for a diverse and inclusive workplace.",
            3: "A company's dedication to Diversity and Inclusion is quite important to you, reflecting your desire for an inclusive and equitable work environment.",
            4: "You highly value a company's ongoing commitment to Diversity and Inclusion programs, viewing them as crucial for fostering an inclusive culture.",
            5: "Extremely high importance is placed on a company's investment in Diversity and Inclusion, indicating a strong preference for working in a diverse and inclusive environment."
        },
        "A company that encourages you to share your opinions at work": {
            0: "Encouragement to share opinions at work is not a major factor for you, suggesting comfort with existing communication channels or other priorities.",
            1: "You see some value in being encouraged to share your opinions, but it's not a major aspect of your job engagement.",
            2: "You moderately value a work environment where sharing opinions is encouraged, considering it important for open communication and collaboration.",
            3: "Being encouraged to share your opinions at work is quite important to you, reflecting your preference for a communicative and open work culture.",
            4: "You highly value a company that encourages the sharing of opinions, seeing it as essential for employee engagement and a healthy work environment.",
            5: "Extremely high importance is placed on the encouragement to share your opinions at work, indicating a strong preference for a workplace that values open dialogue and employee input."
        },
        "Opportunities for social connection at work": {
            0: "Opportunities for social connection at work are not a significant priority for you, suggesting other aspects of your job are more important.",
            1: "You find some value in social connection opportunities at work, but they're not a central aspect of your job satisfaction.",
            2: "You moderately value opportunities for social connection at work, considering them beneficial for team cohesion and workplace enjoyment.",
            3: "Social connection opportunities at work are quite important to you, reflecting your desire for a collaborative and friendly work environment.",
            4: "You highly value opportunities for social interaction at work, seeing them as crucial for your job enjoyment and team dynamics.",
            5: "Extremely high importance is placed on opportunities for social connection at work, indicating a strong preference for a workplace that fosters camaraderie and team bonding."
        },
        "A company that invests in Corporate Social Responsibility programs": {
            0: "Investment in Corporate Social Responsibility programs is not a key priority for you, suggesting other company attributes are more significant.",
            1: "You see some value in a company's Corporate Social Responsibility initiatives, but it's not a major factor in your job satisfaction.",
            2: "You moderately value a company's investment in Corporate Social Responsibility, considering it an important aspect of ethical business practices.",
            3: "Corporate Social Responsibility is quite important to you, reflecting your preference for companies that are socially responsible and ethical.",
            4: "You highly value a company's commitment to Corporate Social Responsibility, viewing it as crucial for aligning with your personal values and ethics.",
            5: "Extremely high importance is placed on a company's Corporate Social Responsibility programs, indicating a strong preference for working at a company that actively contributes to societal good."
        }
    },
    "Job Security and Stability": {
        "A company that prioritizes stability over rapid growth": {
            0: "Prioritizing stability over rapid growth is not a major factor for you, suggesting you're comfortable with a dynamic or changing environment.",
            1: "You find some value in company stability, but it's not a central factor in your job choice.",
            2: "You moderately value a company that prioritizes stability, considering it an important aspect of job security.",
            3: "A company's focus on stability over rapid growth is quite important to you, reflecting your preference for a steady and predictable work environment.",
            4: "You highly value a company that prioritizes stability, viewing it as crucial for your long-term job security and peace of mind.",
            5: "Extremely high importance is placed on company stability over rapid growth, indicating a strong preference for a secure and stable work environment."
        },
        "A job that is unlikely to be automated in the foreseeable future": {
            0: "The likelihood of your job being automated is not a significant concern for you, suggesting confidence in your adaptability or role.",
            1: "You recognize some importance in job security against automation, but it's not a major factor in your career planning.",
            2: "You moderately value having a job that's unlikely to be automated, considering it beneficial for long-term job security.",
            3: "Having a job secure against automation is quite important to you, reflecting your concern for future job stability in a changing workforce.",
            4: "You highly value a role that's unlikely to be automated, seeing it as essential for your long-term career stability.",
            5: "Extremely high importance is placed on having a job that's unlikely to be automated, indicating a strong desire for a secure and future-proof career."
        },
        "Knowing I could have a job with the same company for the rest of my working years": {
            0: "Long-term employment with the same company is not a key priority for you, suggesting a preference for flexibility or varied experiences.",
            1: "You find some value in the possibility of long-term employment with one company, but it's not a central aspect of your career goals.",
            2: "You moderately value the idea of staying with the same company for the rest of your working years, considering it important for stability.",
            3: "Knowing you could stay with the same company for the rest of your career is quite important to you, reflecting your desire for job security and loyalty.",
            4: "You highly value the potential for long-term employment with a single company, viewing it as crucial for your career stability and satisfaction.",
            5: "Extremely high importance is placed on the opportunity for lifelong employment with the same company, indicating a strong preference for stability and long-term career planning."
        },
        "An industry that can withstand an economic downturn": {
            0: "Working in an industry resilient to economic downturns is not a significant factor for you, suggesting confidence in your skills or adaptability.",
            1: "You see some importance in being in an industry that can withstand economic challenges, but it's not a major factor in your career choice.",
            2: "You moderately value being part of an industry that's resilient to economic downturns, considering it an important aspect of job security.",
            3: "Being in an industry that can withstand economic downturns is quite important to you, reflecting your concern for stability and security.",
            4: "You highly value working in an industry known for its resilience to economic challenges, seeing it as essential to your long-term career security.",
            5: "Extremely high importance is placed on being in an industry that can withstand economic downturns, indicating a strong preference for secure and stable industry employment."
        },
        "A job with a consistent workload": {
            0: "Having a consistent workload is not a key priority for you, suggesting you are adaptable to varying work demands.",
            1: "You find some value in a consistent workload, but it's not a central aspect of your job satisfaction.",
            2: "You moderately value having a job with a consistent workload, considering it important for predictability and planning in your work life.",
            3: "A consistent workload is quite important to you, reflecting your preference for stability and predictability in your job.",
            4: "You highly value a job with a consistent workload, viewing it as crucial for your work-life balance and stress management.",
            5: "Extremely high importance is placed on having a consistent workload, indicating a strong preference for a stable and predictable work environment."
        }
    },
    "Manager Relationship": {
        "A manager who empowers me to make decisions on my own": {
            0: "Having a manager who empowers you to make independent decisions is not a significant factor for you, suggesting self-sufficiency or different priorities.",
            1: "You find some value in managerial empowerment for decision-making, but it's not a major factor in your job satisfaction.",
            2: "You moderately value a manager who empowers you to make your own decisions, considering it important for autonomy and confidence in your role.",
            3: "Managerial empowerment for independent decision-making is quite important to you, reflecting your desire for autonomy and trust in your job.",
            4: "You highly value a manager who empowers you to make decisions, viewing it as crucial for your professional development and job satisfaction.",
            5: "Extremely high importance is placed on having a manager who empowers independent decision-making, indicating a strong preference for autonomy and self-leadership in your role."
        },
        "A manager who provides performance feedback to me": {
            0: "Receiving performance feedback from your manager is not a key priority for you, suggesting other forms of job satisfaction or self-assessment.",
            1: "You find some value in receiving performance feedback, but it's not a central aspect of your job engagement.",
            2: "You moderately value receiving performance feedback from your manager, considering it beneficial for your professional growth.",
            3: "Regular performance feedback from your manager is quite important to you, reflecting your desire for continual improvement and recognition.",
            4: "You highly value a manager who provides consistent performance feedback, seeing it as essential to your career development and achievement.",
            5: "Extremely high importance is placed on receiving performance feedback from your manager, indicating a strong preference for regular evaluation and guidance."
        },
        "A manager who provides recognition for my accomplishments": {
            0: "Managerial recognition of your accomplishments is not a significant factor for you, suggesting self-motivation or different priorities.",
            1: "You see some value in receiving recognition from your manager, but it's not a major factor in your job satisfaction.",
            2: "You moderately value recognition from your manager for your achievements, considering it an important aspect of your work life.",
            3: "Receiving recognition from your manager for your accomplishments is quite important to you, reflecting your need for acknowledgement and motivation.",
            4: "You highly value a manager who recognizes your accomplishments, viewing it as crucial to your job satisfaction and motivation.",
            5: "Extremely high importance is placed on managerial recognition for your accomplishments, indicating a strong desire for acknowledgment and appreciation in your role."
        },
        "A manager who supports my career development": {
            0: "Managerial support for your career development is not a key concern for you, suggesting self-direction or other priorities.",
            1: "You find some value in having a manager who supports your career development, but it's not a major factor in your job satisfaction.",
            2: "You moderately value a manager who supports your career development, considering it beneficial for your professional growth and opportunities.",
            3: "A manager who actively supports your career development is quite important to you, reflecting your desire for guidance and progression in your career.",
            4: "You highly value a manager who is supportive of your career development, seeing it as essential for your long-term career goals and satisfaction.",
            5: "Extremely high importance is placed on having a manager who supports your career development, indicating a strong preference for mentorship and growth opportunities."
        },
        "A manager who wants to get to know me as a person, not just an employee": {
            0: "A manager who seeks to know you personally is not a significant factor in your job satisfaction, suggesting a preference for professional boundaries.",
            1: "You see some importance in having a manager who wants to know you personally, but it's not a central aspect of your work relationship.",
            2: "You moderately value a manager who takes an interest in you as a person, considering it important for a positive and engaging work environment.",
            3: "Having a manager who wants to know you beyond your professional role is quite important to you, reflecting your preference for a more personalized and empathetic management style.",
            4: "You highly value a manager who takes the time to know you personally, viewing it as crucial for a meaningful and supportive work relationship.",
            5: "Extremely high importance is placed on having a manager who wants to understand you as a person, indicating a strong preference for a close and empathetic managerial relationship."
        },
        "A manager who provides stretch opportunities to learn new skills": {
            0: "Receiving stretch opportunities from your manager is not a major priority for you, suggesting satisfaction with your current skill set or other learning methods.",
            1: "You find some value in stretch opportunities for learning new skills, but they're not a central aspect of your job growth.",
            2: "You moderately value stretch opportunities from your manager to learn new skills, considering them important for your professional development.",
            3: "Having a manager who provides opportunities to expand your skills is quite important to you, reflecting your desire for continual learning and growth.",
            4: "You highly value a manager who offers stretch opportunities for skill development, seeing it as essential for your career progression and adaptability.",
            5: "Extremely high importance is placed on receiving stretch opportunities from your manager, indicating a strong desire for ongoing skill development and challenging experiences."
        }
    },
    "Meaningful Work": {
        "A job that has a positive impact on the lives of others": {
            0: "Having a job that positively impacts others is not a primary factor for you, suggesting other aspects of work are more significant.",
            1: "You find some value in having a job that impacts others positively, but it's not a central aspect of your job satisfaction.",
            2: "You moderately value a job that has a positive impact on the lives of others, considering it important for personal fulfillment.",
            3: "Having a job that positively affects others is quite important to you, reflecting your desire for meaningful and impactful work.",
            4: "You highly value a job that makes a positive impact on others, seeing it as essential to your sense of purpose and job satisfaction.",
            5: "Extremely high importance is placed on having a job that impacts the lives of others positively, indicating a strong preference for work that contributes significantly to societal well-being."
        },
        "A company with an inspiring mission and purpose": {
            0: "Working for a company with an inspiring mission is not a significant priority for you, suggesting other factors are more important.",
            1: "You see some importance in a company's inspiring mission, but it's not a major factor in your career choice.",
            2: "You moderately value a company's mission and purpose, considering it an important aspect of your alignment with the company.",
            3: "An inspiring company mission and purpose is quite important to you, reflecting your desire for work that aligns with larger goals and values.",
            4: "You highly value a company with an inspiring mission and purpose, viewing it as crucial for your engagement and commitment to your work.",
            5: "Extremely high importance is placed on a company's mission and purpose, indicating a strong preference for working in an environment driven by inspiring and meaningful goals."
        },
        "A company whose products have a positive impact on the world": {
            0: "A company's positive global impact through its products is not a key factor for you, suggesting other job aspects are more significant.",
            1: "You find some value in a company whose products positively impact the world, but it's not a central factor in your job satisfaction.",
            2: "You moderately value a company's positive impact on the world through its products, considering it important for ethical and social responsibility.",
            3: "A company that creates products with a positive global impact is quite important to you, reflecting your preference for socially responsible and beneficial work.",
            4: "You highly value a company whose products have a positive impact on the world, seeing it as essential for your alignment with the company's values.",
            5: "Extremely high importance is placed on a company's global impact through its products, indicating a strong desire to contribute to work that makes a significant positive difference."
        },
        "A company that is committed to environmental sustainability": {
            0: "A company's commitment to environmental sustainability is not a significant concern for you, indicating other priorities or values.",
            1: "You see some importance in environmental sustainability, but it's not a major factor in your alignment with a company.",
            2: "You moderately value a company's commitment to environmental sustainability, considering it an important aspect of corporate responsibility.",
            3: "Environmental sustainability is quite important to you in a company, reflecting your concern for ecological well-being and ethical business practices.",
            4: "You highly value a company's commitment to environmental sustainability, viewing it as crucial for your support and engagement with the company.",
            5: "Extremely high importance is placed on a company's commitment to environmental sustainability, indicating a strong preference for working in an eco-conscious and responsible organization."
        },
        "A job that provides meaning and purpose in my life": {
            0: "Having a job that provides personal meaning and purpose is not a key priority for you, suggesting satisfaction with other aspects of your work.",
            1: "You find some value in having a job that provides meaning, but it's not a central aspect of your career fulfillment.",
            2: "You moderately value a job that gives you a sense of purpose, considering it beneficial for your overall job satisfaction and well-being.",
            3: "A job that provides personal meaning and purpose is quite important to you, reflecting your desire for work that aligns with your values and passions.",
            4: "You highly value a job that offers a sense of meaning and purpose, seeing it as essential for your fulfillment and happiness in your career.",
            5: "Extremely high importance is placed on having a job that provides meaning and purpose, indicating a strong preference for work that deeply aligns with your personal values and aspirations."
        }
    },
    "Personal Impact": {
        "Having important responsibilities in my job": {
            0: "Having important responsibilities at work is not a primary concern for you, suggesting other aspects of your job are more significant.",
            1: "You find some value in having important responsibilities, but it's not a central aspect of your job satisfaction.",
            2: "You moderately value having important responsibilities in your job, considering it beneficial for your sense of involvement and importance.",
            3: "Important responsibilities in your job are quite important to you, reflecting your desire for a significant role in your work environment.",
            4: "You highly value having important responsibilities at work, viewing them as crucial to your feeling of achievement and job satisfaction.",
            5: "Extremely high importance is placed on having important responsibilities, indicating a strong preference for a role where your contributions are crucial and recognized."
        },
        "Mentoring others at work": {
            0: "Mentoring others at work is not a significant factor in your job satisfaction, suggesting other priorities or job aspects are more important.",
            1: "You see some value in mentoring others, but it's not a major aspect of your professional life.",
            2: "You moderately value the opportunity to mentor others at work, considering it beneficial for team development and personal fulfillment.",
            3: "Being a mentor at work is quite important to you, reflecting your interest in leadership and contributing to others' growth.",
            4: "You highly value the role of mentoring others, seeing it as essential to your professional identity and the impact you have on your team.",
            5: "Extremely high importance is placed on mentoring others at work, indicating a strong desire to contribute to the development and success of your colleagues."
        },
        "Work that directly impacts customers": {
            0: "Directly impacting customers through your work is not a primary focus for you, suggesting other job elements are more significant.",
            1: "You find some value in work that impacts customers, but it's not a central factor in your job satisfaction.",
            2: "You moderately value having a direct impact on customers, considering it an important aspect of your professional effectiveness.",
            3: "Work that has a direct impact on customers is quite important to you, reflecting your desire to contribute meaningfully to customer experience.",
            4: "You highly value work that directly impacts customers, viewing it as crucial to your sense of accomplishment and the value you bring to your job.",
            5: "Extremely high importance is placed on work that impacts customers directly, indicating a strong preference for roles that directly influence customer satisfaction and experience."
        },
        "Feeling a sense of accomplishment in my job": {
            0: "Feeling a sense of accomplishment in your job is not a significant priority, suggesting other aspects of work are more important to you.",
            1: "You recognize some importance in feeling accomplished, but it's not a major factor in your overall job satisfaction.",
            2: "You moderately value a sense of accomplishment in your job, considering it important for your motivation and professional fulfillment.",
            3: "Feeling a sense of accomplishment is quite important to you, reflecting your need for recognition and validation of your work efforts.",
            4: "You highly value a strong sense of accomplishment in your job, seeing it as essential to your happiness and success in your role.",
            5: "Extremely high importance is placed on feeling accomplished in your job, indicating a strong desire for work that consistently provides a sense of achievement and fulfillment."
        },
        "Work that directly impacts the success of the company": {
            0: "Having work that directly impacts the company's success is not a key factor for you, suggesting satisfaction with contributing in other ways.",
            1: "You find some value in having work that impacts the company's success, but it's not a central aspect of your job satisfaction.",
            2: "You moderately value work that contributes directly to the company's success, considering it an important part of your role and contribution.",
            3: "Work that directly affects the success of the company is quite important to you, reflecting your desire to be an integral part of the company's achievements.",
            4: "You highly value having work that directly impacts the company's success, viewing it as crucial to your sense of purpose and contribution.",
            5: "Extremely high importance is placed on work that directly influences the success of the company, indicating a strong preference for a role where your contributions are pivotal."
        },
        "Leaving a legacy behind after I've left the company": {
            0: "Leaving a legacy behind is not a significant concern for you, suggesting other aspects of your job are more important.",
            1: "You see some importance in the idea of leaving a legacy, but it's not a major factor in your career planning.",
            2: "You moderately value the concept of leaving a lasting impact after leaving a company, considering it a meaningful aspect of your career.",
            3: "Leaving a legacy is quite important to you, reflecting your desire to make a lasting impact and be remembered for your contributions.",
            4: "You highly value the opportunity to leave a legacy behind, seeing it as essential to your personal and professional fulfillment.",
            5: "Extremely high importance is placed on leaving a legacy at your company, indicating a strong desire to make enduring contributions and be remembered for your impact."
        }
    }



    }

    responses = {category: {} for category in categories}

    for category, questions in categories.items():
        print(f"\nCategory: {category}")
        for question in questions:
            responses[category][question] = get_user_input(question)

    category_reports = generate_report(responses, report_messages)

    # Calculate average ratings for graphing
     # Calculate average ratings
    average_ratings = {category: sum(questions.values()) / len(questions) for category, questions in responses.items()}

    sorted_motivators = sorted(average_ratings.items(), key=lambda x: x[1], reverse=True)

    # Scale the ratings
    average_ratings_scaled = {cat: round(avg * 20) for cat, avg in average_ratings.items()}
    categories_list = list(average_ratings.keys())
    averages = list(average_ratings.values())

    average_ratings_scaled = {cat: round(avg * 20) for cat, avg in average_ratings.items()}
    sorted_categories = sorted(average_ratings_scaled.items(), key=lambda x: x[1], reverse=True)
    top_motivators = sorted_categories[:3]
    middling_motivators = sorted_categories[3:6]
    lowest_motivators = sorted_categories[6:]

    # Create a PDF file
    base_filename = "Employee_Satisfaction_Report"
    counter = 1
    filename = f"{base_filename}.pdf"
    while os.path.exists(filename):
        filename = f"{base_filename}_{counter}.pdf"
        counter += 1

    c = canvas.Canvas(filename, pagesize=letter)
    c.setFont("Helvetica", 12)
    y_position = 750

    c.drawString(100, y_position, "Your Personalized Motivations Report")
    y_position -= 20

    
    y_position = add_motivators_to_pdf(top_motivators, "Your Top Motivators", y_position, category_reports,c)
    y_position = add_motivators_to_pdf(middling_motivators, "Your Middling Motivators", y_position, category_reports,c)
    y_position = add_motivators_to_pdf(lowest_motivators, "Your Lowest Motivators", y_position, category_reports,c)

    # Start a new page for detailed reports
    if y_position < 300:
        c.showPage()
        y_position = 750


# Iterate over each category and its report
   
    # Graphing
    plt.figure(figsize=(10, 6))
    plt.bar(categories_list, averages, color='skyblue')
    plt.xlabel('Categories')
    plt.ylabel('Average Rating')
    plt.title('Average User Ratings per Category')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Save the bar chart to a temporary file
    bar_chart_temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
    plt.savefig(bar_chart_temp_file.name)
    bar_chart_path = bar_chart_temp_file.name
    # Draw the bar chart on the current page
    c.drawImage(bar_chart_path, 100, 300, width=400, height=300)

    # Create a new page for the radar chart
    c.showPage()

    # Generate and draw radar chart
    radar_chart_filename = "/tmp/radar_chart.png"
    create_radar_chart(categories_list, averages, radar_chart_filename)
    c.drawImage(radar_chart_filename, 100, 300, width=400, height=300)

    # Finalize the PDF
    c.showPage()
    c.save()

    # Cleanup temporary files
    os.remove(bar_chart_path)

if __name__ == "__main__":
    main()