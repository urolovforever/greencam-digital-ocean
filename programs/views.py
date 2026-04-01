from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.utils.translation import get_language
from django.core.paginator import Paginator
from .models import Program


WP_DATA = {
    1: {
        'num': 1,
        'title': 'Project Management and Quality Assurance',
        'title_uz': 'Loyiha boshqaruvi va sifat nazorati',
        'lead': 'KU (Kokand University)',
        'lead_uz': 'KU (Qo\'qon Universiteti)',
        'duration': 'M1 – M36',
        'effort': '25 person-months',
        'effort_uz': '25 kishi-oy',
        'participants': 'All partners',
        'participants_uz': 'Barcha hamkorlar',
        'description': 'Management Handbook will be developed, describing the project management and organization structure defining roles, and assigning responsibilities to the involved partner institutions. It will also describe the mechanism and procedures of project work organization and provide the necessary documents and templates. Partnership Agreement that each partner and coordinator will sign soon after the Grant Agreement signature. During the project, 5 face-to-face meetings, 2 online meetings, 3 conferences, 3 training events, and 6 workshops for ambassadors will be organized and disseminated. Financial statements will be structured and delivered according to the reporting rules of the EACEA Erasmus+ program. The coordinator will submit project periodic reports on time to the European Commission, according to the reporting guidelines.',
        'description_uz': 'Boshqaruv qo\'llanmasi ishlab chiqiladi, unda loyihani boshqarish va tashkiliy tuzilma, rollar va hamkor muassasalarga mas\'uliyatlar belgilanadi. U loyiha ishini tashkil etish mexanizmi va tartiblarini tavsiflaydi, zarur hujjatlar va shablonlarni taqdim etadi. Loyiha davomida 5 ta yuzma-yuz uchrashuv, 2 ta onlayn uchrashuv, 3 ta konferensiya, 3 ta trening tadbiri va elchilar uchun 6 ta seminar tashkil etiladi.',
        'tasks': [
            {'num': '1.1', 'title': 'Establish the project management structure and procedure.', 'title_uz': 'Loyiha boshqaruv tuzilmasi va tartibini yaratish.', 'deliverable': 'Project management handbook (D1.1, M6)', 'deliverable_uz': 'Loyiha boshqaruvi qo\'llanmasi (D1.1, M6)'},
            {'num': '1.2', 'title': 'Organising kick-off meetings and regular coordination meetings.', 'title_uz': 'Boshlang\'ich va muntazam koordinatsiya uchrashuvlarini tashkil etish.', 'deliverable': 'Meeting reports', 'deliverable_uz': 'Uchrashuv hisobotlari'},
            {'num': '1.3', 'title': 'Financial management and reporting. Final report.', 'title_uz': 'Moliyaviy boshqaruv va hisobot. Yakuniy hisobot.', 'deliverable': 'Progress Report (D1.3, M18)', 'deliverable_uz': 'Taraqqiyot hisoboti (D1.3, M18)'},
            {'num': '1.4', 'title': 'Progress monitoring and evaluation of quality assurance.', 'title_uz': 'Taraqqiyotni monitoring qilish va sifat nazoratini baholash.', 'deliverable': 'Quality assurance plan (D1.2, M6), Mid-term QA report (D1.4, M18), Final QA report (D1.5, M36)', 'deliverable_uz': 'Sifat nazorati rejasi (D1.2, M6), O\'rta muddatli sifat hisoboti (D1.4, M18), Yakuniy sifat hisoboti (D1.5, M36)'},
        ],
    },
    2: {
        'num': 2,
        'title': 'Green Campus Strategy Development',
        'title_uz': 'Yashil kampus strategiyasini ishlab chiqish',
        'lead': 'GSBE (Graduate School of Business and Entrepreneurship)',
        'lead_uz': 'GSBE (Biznes va Tadbirkorlik Oliy Maktabi)',
        'duration': 'M1 – M12',
        'effort': '15 person-months',
        'effort_uz': '15 kishi-oy',
        'participants': 'All partners',
        'participants_uz': 'Barcha hamkorlar',
        'description': 'Develop and implement comprehensive green campus strategies for 6 participating Uzbek universities. Creation of implementation roadmaps for the implementation of the strategy at partner UZ institutions. The creation of a framework for monitoring and assessment of the green campus initiatives. Setting up sustainability indicators and targets.',
        'description_uz': 'O\'zbekistonning 6 ta ishtirokchi universiteti uchun keng qamrovli yashil kampus strategiyalarini ishlab chiqish va joriy etish. Hamkor O\'zbekiston muassasalarida strategiyani amalga oshirish uchun yo\'l xaritalarini yaratish. Yashil kampus tashabbuslarini monitoring qilish va baholash tizimini yaratish.',
        'tasks': [
            {'num': '2.1', 'title': 'Development of comprehensive green campus strategies for 6 universities.', 'title_uz': '6 ta universitet uchun keng qamrovli yashil kampus strategiyalarini ishlab chiqish.', 'deliverable': 'Green campus strategies (D2.1, M12, Public)', 'deliverable_uz': 'Yashil kampus strategiyalari (D2.1, M12, Ommaviy)'},
            {'num': '2.2', 'title': 'Creation of implementation roadmaps.', 'title_uz': 'Amalga oshirish yo\'l xaritalarini yaratish.', 'deliverable': 'Roadmap documents', 'deliverable_uz': 'Yo\'l xaritasi hujjatlari'},
            {'num': '2.3', 'title': 'Establishment of monitoring and evaluation framework.', 'title_uz': 'Monitoring va baholash tizimini yaratish.', 'deliverable': 'M&E framework with sustainability indicators', 'deliverable_uz': 'Barqarorlik ko\'rsatkichlari bilan M&E tizimi'},
        ],
    },
    3: {
        'num': 3,
        'title': 'Curriculum Development and Integration',
        'title_uz': 'O\'quv dasturlarni ishlab chiqish va integratsiya',
        'lead': 'ASTI (Andijan State Technical Institute)',
        'lead_uz': 'ASTI (Andijon davlat texnika instituti)',
        'duration': 'M6 – M24',
        'effort': '27 person-months',
        'effort_uz': '27 kishi-oy',
        'participants': 'All partners',
        'participants_uz': 'Barcha hamkorlar',
        'description': 'The creation of 12 courses/modules that concentrate on sustainability and the development of teaching materials and resources. The addition of new and updated courses to current programs. All partners will participate in two waves of testing. Courses will be tested by instructors, professionals, and officials first. Second, students will test courses during instruction.',
        'description_uz': 'Barqarorlikka yo\'naltirilgan 12 ta kurs/modulni yaratish va o\'quv materiallar hamda resurslarni ishlab chiqish. Yangi va yangilangan kurslarni mavjud dasturlarga qo\'shish. Barcha hamkorlar ikki bosqichli sinovda ishtirok etadilar.',
        'tasks': [
            {'num': '3.1', 'title': 'Development of 12 sustainability-focused courses/modules and creation of teaching materials and resources.', 'title_uz': '12 ta barqarorlikka yo\'naltirilgan kurs/modul va o\'quv materiallarni ishlab chiqish.', 'deliverable': '12 sustainability focused courses (D3.1, M24, Public)', 'deliverable_uz': '12 ta barqarorlikka yo\'naltirilgan kurslar (D3.1, M24, Ommaviy)'},
            {'num': '3.2', 'title': 'Integration of new courses into existing programs.', 'title_uz': 'Yangi kurslarni mavjud dasturlarga integratsiya qilish.', 'deliverable': 'Updated programs (D3.2, M24, Sensitive)', 'deliverable_uz': 'Yangilangan dasturlar (D3.2, M24)'},
            {'num': '3.3', 'title': 'Pilot testing of new courses.', 'title_uz': 'Yangi kurslarni sinov qilish.', 'deliverable': 'Feedback report based on testing process', 'deliverable_uz': 'Sinov jarayoni bo\'yicha teskari aloqa hisoboti'},
        ],
    },
    4: {
        'num': 4,
        'title': 'Capacity Building and Training',
        'title_uz': 'Salohiyat oshirish va trening',
        'lead': 'AFU (Alfraganus University)',
        'lead_uz': 'AFU (Alfraganus University)',
        'duration': 'M6 – M24',
        'effort': '10 person-months',
        'effort_uz': '10 kishi-oy',
        'participants': 'All partners',
        'participants_uz': 'Barcha hamkorlar',
        'description': 'Developing the 3 specialized training programs on sustainable practices and green technologies by EU partners based on the needs of UZ partners. Organizing the 3 training events at OUTech (Politechnika Opolska), KBU, and GSBE. The workshops are held at each UZ partner that selects the attendees according to the agreed criteria, provides the timetable of the lectures, ensures the presence list is signed, distributes the training material package and the feedback questionnaire, records the presentations, drafts an evaluation report during the M18-M20.',
        'description_uz': 'O\'zbekiston hamkorlarining ehtiyojlari asosida Yevropa hamkorlari tomonidan barqaror amaliyotlar va yashil texnologiyalar bo\'yicha 3 ta maxsus trening dasturini ishlab chiqish. OUTech, KBU va GSBE da 3 ta trening tadbirini tashkil etish.',
        'tasks': [
            {'num': '4.1', 'title': 'Development of 3 specialized training courses.', 'title_uz': '3 ta maxsus trening kursini ishlab chiqish.', 'deliverable': '3 training courses and training events (D4.1, M24, Sensitive)', 'deliverable_uz': '3 ta trening kursi va trening tadbirlari (D4.1, M24)'},
            {'num': '4.2', 'title': 'Training of 48 faculty members and 24 administrative staff.', 'title_uz': '48 ta professor-o\'qituvchi va 24 ta ma\'muriy xodimni o\'qitish.', 'deliverable': 'Training completion reports', 'deliverable_uz': 'Trening yakunlanishi hisobotlari'},
            {'num': '4.3', 'title': 'Green Campus Ambassador Program development and training of 60+60 green campus ambassadors.', 'title_uz': 'Green Campus Ambassador dasturini ishlab chiqish va 60+60 elchini o\'qitish.', 'deliverable': 'Green Campus Ambassador Program and sessions (D4.2, M24, Public)', 'deliverable_uz': 'Green Campus Ambassador dasturi va sessiyalari (D4.2, M24, Ommaviy)'},
        ],
    },
    5: {
        'num': 5,
        'title': 'Sustainable Infrastructure Implementation',
        'title_uz': 'Barqaror infratuzilmani joriy etish',
        'lead': 'TIU (Tashkent International University)',
        'lead_uz': 'TIU (Tashkent International University)',
        'duration': 'M12 – M24',
        'effort': '33 person-months',
        'effort_uz': '33 kishi-oy',
        'participants': 'All partners',
        'participants_uz': 'Barcha hamkorlar',
        'description': 'Each UZ partner will design and implement the pilot project and share the results. Based on the results, best practices documentation will be developed.',
        'description_uz': 'Har bir O\'zbekiston hamkori pilot loyihani loyihalaydi va amalga oshiradi, natijalarni ulashadi. Natijalar asosida eng yaxshi amaliyotlar hujjatlari ishlab chiqiladi.',
        'tasks': [
            {'num': '5.1', 'title': 'Design and implementation of 6 pilot projects (one at each UZ partner).', 'title_uz': '6 ta pilot loyihani loyihalash va amalga oshirish (har bir O\'zbekiston hamkorida bittadan).', 'deliverable': '6 pilot project implementations (D5.1, M24, Public)', 'deliverable_uz': '6 ta pilot loyiha amalga oshirilishi (D5.1, M24, Ommaviy)'},
            {'num': '5.2', 'title': 'Technical documentation and guidelines.', 'title_uz': 'Texnik hujjatlar va ko\'rsatmalar.', 'deliverable': 'Best practices documentation (D5.2, M24, Public)', 'deliverable_uz': 'Eng yaxshi amaliyotlar hujjatlari (D5.2, M24, Ommaviy)'},
        ],
    },
    6: {
        'num': 6,
        'title': 'Community Engagement and Networking',
        'title_uz': 'Jamoatchilik ishtiroki va tarmoqlashtirish',
        'lead': 'CAGU (Central Asian University / Green University)',
        'lead_uz': 'CAGU (Markaziy Osiyo Universiteti / Green University)',
        'duration': 'M6 – M34',
        'effort': '21 person-months',
        'effort_uz': '21 kishi-oy',
        'participants': 'All partners',
        'participants_uz': 'Barcha hamkorlar',
        'description': 'All UZ partners will sign the 2 partnership agreements with business and community organizations. Every year the annual Green Conference will be held at AFU, TIU, and KU. 1000 users engaged on the virtual platform for knowledge-sharing.',
        'description_uz': 'Barcha O\'zbekiston hamkorlari biznes va jamoat tashkilotlari bilan 2 tadan hamkorlik shartnomasini imzoladilar. Har yili yillik Green Conference AFU, TIU va KU da o\'tkaziladi. Virtual platformada 1000 foydalanuvchi jalb etiladi.',
        'tasks': [
            {'num': '6.1', 'title': 'Development of a virtual knowledge-sharing platform.', 'title_uz': 'Virtual bilim almashish platformasini yaratish.', 'deliverable': 'Virtual platform with 1000 users (D6.1, M12, Public)', 'deliverable_uz': '1000 foydalanuvchili virtual platforma (D6.1, M12, Ommaviy)'},
            {'num': '6.2', 'title': 'Establishment of business and community partnerships.', 'title_uz': 'Biznes va jamoat hamkorliklarini o\'rnatish.', 'deliverable': 'Partnership agreements report (D6.2, M12, Sensitive)', 'deliverable_uz': 'Hamkorlik shartnomalar hisoboti (D6.2, M12)'},
            {'num': '6.3', 'title': 'Organization of Green Campus Conference year 1 at AFU (200+ participants).', 'title_uz': 'AFU da Green Campus konferensiyasi 1-yil (200+ ishtirokchi).', 'deliverable': 'Conference Book (D6.3, M12, Public)', 'deliverable_uz': 'Konferensiya kitobi (D6.3, M12, Ommaviy)'},
            {'num': '6.4', 'title': 'Organization of Green Campus Conference year 2 at TIU (200+ participants).', 'title_uz': 'TIU da Green Campus konferensiyasi 2-yil (200+ ishtirokchi).', 'deliverable': 'Conference Book (D6.4, M24, Public)', 'deliverable_uz': 'Konferensiya kitobi (D6.4, M24, Ommaviy)'},
            {'num': '6.5', 'title': 'Organization of Green Campus Conference year 3 at KU (200+ participants).', 'title_uz': 'KU da Green Campus konferensiyasi 3-yil (200+ ishtirokchi).', 'deliverable': 'Conference Book (D6.5, M34, Public)', 'deliverable_uz': 'Konferensiya kitobi (D6.5, M34, Ommaviy)'},
        ],
    },
    7: {
        'num': 7,
        'title': 'Impact and Dissemination',
        'title_uz': 'Ta\'sir va tarqatish',
        'lead': 'TIU (Tashkent International University)',
        'lead_uz': 'TIU (Tashkent International University)',
        'duration': 'M1 – M36',
        'effort': '30 person-months',
        'effort_uz': '30 kishi-oy',
        'participants': 'All partners',
        'participants_uz': 'Barcha hamkorlar',
        'description': 'A dissemination strategy, sustainability, and exploitation plan will be developed. The project website and logo will be developed and launched. The structure of the website will be established from the first phases of the project. All outputs will be launched on the website.',
        'description_uz': 'Tarqatish strategiyasi, barqarorlik va foydalanish rejasi ishlab chiqiladi. Loyiha veb-sayti va logotipi ishlab chiqiladi va ishga tushiriladi. Barcha natijalar veb-saytda joylashtriladi.',
        'tasks': [
            {'num': '7.1', 'title': 'Development of dissemination strategy.', 'title_uz': 'Tarqatish strategiyasini ishlab chiqish.', 'deliverable': 'Dissemination strategy (D7.1, M6, Sensitive)', 'deliverable_uz': 'Tarqatish strategiyasi (D7.1, M6)'},
            {'num': '7.2', 'title': 'Creation of sustainability and exploitation plan.', 'title_uz': 'Barqarorlik va foydalanish rejasini yaratish.', 'deliverable': 'Sustainability and Exploitation Plan (D7.2, M6, Sensitive)', 'deliverable_uz': 'Barqarorlik va foydalanish rejasi (D7.2, M6)'},
            {'num': '7.3', 'title': 'Creation of project website, social media presence, and promotional materials.', 'title_uz': 'Loyiha veb-sayti, ijtimoiy tarmoqlar va reklama materiallarini yaratish.', 'deliverable': 'Project website (D7.3, M6, Public)', 'deliverable_uz': 'Loyiha veb-sayti (D7.3, M6, Ommaviy)'},
            {'num': '7.4', 'title': 'Mid-term dissemination reporting.', 'title_uz': 'O\'rta muddatli tarqatish hisoboti.', 'deliverable': 'Mid-term Dissemination & Exploitation report (D7.4, M18, Public)', 'deliverable_uz': 'O\'rta muddatli tarqatish va foydalanish hisoboti (D7.4, M18, Ommaviy)'},
            {'num': '7.5', 'title': 'Final dissemination reporting.', 'title_uz': 'Yakuniy tarqatish hisoboti.', 'deliverable': 'Final Dissemination & Exploitation report (D7.5, M36, Public)', 'deliverable_uz': 'Yakuniy tarqatish va foydalanish hisoboti (D7.5, M36, Ommaviy)'},
        ],
    },
}


def _get_wp_translated(wp_data):
    """Return WP data dict with translated fields based on current language."""
    lang = get_language() or 'en'
    if lang != 'uz':
        return wp_data
    result = dict(wp_data)
    for field in ('title', 'lead', 'description', 'effort', 'participants'):
        uz_val = wp_data.get(f'{field}_uz', '')
        if uz_val:
            result[field] = uz_val
    result['tasks'] = []
    for task in wp_data.get('tasks', []):
        t = dict(task)
        if task.get('title_uz'):
            t['title'] = task['title_uz']
        if task.get('deliverable_uz'):
            t['deliverable'] = task['deliverable_uz']
        result['tasks'].append(t)
    return result


def program_list(request):
    wp_list = [_get_wp_translated(wp) for wp in WP_DATA.values()]
    return render(request, 'programs_list.html', {'wp_list': wp_list})


def wp_detail(request, wp_num):
    wp = WP_DATA.get(wp_num)
    if not wp:
        raise Http404
    return render(request, 'wp_detail.html', {'wp': _get_wp_translated(wp)})


def program_detail(request, slug):
    program = get_object_or_404(Program, slug=slug, is_active=True)
    return render(request, 'program_detail.html', {'program': program})
