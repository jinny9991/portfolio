import os
from datetime import datetime

class PortfolioGenerator:
    def __init__(self):
        self.portfolio_data = {
            'name': 'Jinhee Park',
            'title': 'Brand Marketing Portfolio',
            'subtitle': '"전략과 실행을 잇는 브랜드 Performer"',
            'keywords': [
                '글로벌 마케팅 | IMC 온오프라인 마케팅 | 디지털 마케팅 | 데이터 기반 브랜드전략가',
                '6년 경력 | 국제 수상 3회 | 검색광고마케터 1급 | 데이터분석 준전문가'
            ],
            'contact': {
                'email': 'jinhee.park@email.com',
                'phone': '+82-10-0000-0000',
                'linkedin': 'https://linkedin.com/in/jinhee-park'
            }
        }
        
    def generate_css(self):
        """CSS 스타일 생성"""
        return """
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        /* Navigation */
        nav {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            z-index: 1000;
            padding: 15px 0;
            box-shadow: 0 2px 20px rgba(0, 0, 0, 0.1);
        }

        nav ul {
            list-style: none;
            display: flex;
            justify-content: center;
            gap: 30px;
        }

        nav a {
            text-decoration: none;
            color: #333;
            font-weight: 500;
            transition: all 0.3s ease;
            padding: 10px 20px;
            border-radius: 25px;
        }

        nav a:hover, nav a.active {
            background: #667eea;
            color: white;
            transform: translateY(-2px);
        }

        /* Hero Section */
        .hero {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 120px 0 80px;
            text-align: center;
            margin-top: 60px;
        }

        .hero h1 {
            font-size: 3.5em;
            margin-bottom: 20px;
            animation: fadeInUp 1s ease-out;
        }

        .hero .subtitle {
            font-size: 1.5em;
            margin-bottom: 30px;
            opacity: 0.9;
            animation: fadeInUp 1s ease-out 0.2s both;
        }

        .hero .keywords {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            padding: 30px;
            border-radius: 15px;
            margin: 40px auto;
            max-width: 800px;
            animation: fadeInUp 1s ease-out 0.4s both;
        }

        .hero .keywords p {
            font-size: 1.1em;
            margin-bottom: 15px;
        }

        /* Section Styles */
        .section {
            background: white;
            margin: 40px 0;
            padding: 60px;
            border-radius: 20px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
            animation: fadeInUp 0.8s ease-out;
        }

        .section h2 {
            color: #667eea;
            font-size: 2.5em;
            margin-bottom: 30px;
            text-align: center;
        }

        .section h3 {
            color: #764ba2;
            font-size: 1.8em;
            margin: 40px 0 20px;
            border-left: 4px solid #667eea;
            padding-left: 20px;
        }

        /* Triangle Visualization */
        .triangle-container {
            text-align: center;
            margin: 40px 0;
            padding: 40px;
            background: #f8f9ff;
            border-radius: 15px;
        }

        .triangle {
            font-size: 1.2em;
            color: #667eea;
            font-weight: bold;
            line-height: 2;
        }

        /* Timeline */
        .timeline {
            position: relative;
            padding: 20px 0;
        }

        .timeline::before {
            content: '';
            position: absolute;
            left: 50%;
            top: 0;
            bottom: 0;
            width: 3px;
            background: linear-gradient(to bottom, #667eea, #764ba2);
            transform: translateX(-50%);
        }

        .timeline-item {
            position: relative;
            margin: 30px 0;
            padding: 20px;
            background: #f8f9ff;
            border-radius: 10px;
            width: 45%;
            animation: slideIn 0.6s ease-out;
        }

        .timeline-item:nth-child(even) {
            margin-left: 55%;
        }

        .timeline-item::before {
            content: '';
            position: absolute;
            width: 15px;
            height: 15px;
            background: #667eea;
            border-radius: 50%;
            top: 25px;
        }

        .timeline-item:nth-child(odd)::before {
            right: -32px;
        }

        .timeline-item:nth-child(even)::before {
            left: -32px;
        }

        /* SWOT Analysis */
        .swot-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin: 30px 0;
        }

        .swot-card {
            background: #f8f9ff;
            padding: 30px;
            border-radius: 15px;
            border-left: 5px solid #667eea;
        }

        .swot-card h4 {
            color: #764ba2;
            margin-bottom: 15px;
            font-size: 1.3em;
        }

        /* Projects Table */
        .projects-table {
            width: 100%;
            border-collapse: collapse;
            margin: 30px 0;
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
        }

        .projects-table th {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 20px;
            text-align: left;
            font-weight: 600;
        }

        .projects-table td {
            padding: 20px;
            border-bottom: 1px solid #eee;
            vertical-align: top;
        }

        .projects-table tr:hover {
            background: #f8f9ff;
            transition: all 0.3s ease;
        }

        .rank-badge {
            background: #667eea;
            color: white;
            padding: 8px 12px;
            border-radius: 20px;
            font-weight: bold;
            text-align: center;
            min-width: 40px;
        }

        /* Animations */
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateX(-20px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .container {
                padding: 10px;
            }

            .hero h1 {
                font-size: 2.5em;
            }

            .hero .subtitle {
                font-size: 1.2em;
            }

            .section {
                padding: 40px 20px;
            }

            nav ul {
                flex-direction: column;
                gap: 10px;
            }

            .timeline::before {
                left: 20px;
            }

            .timeline-item {
                width: calc(100% - 60px);
                margin-left: 60px;
            }

            .timeline-item:nth-child(even) {
                margin-left: 60px;
            }

            .timeline-item::before {
                left: -42px !important;
            }

            .swot-grid {
                grid-template-columns: 1fr;
            }

            .projects-table {
                font-size: 0.9em;
            }

            .projects-table th,
            .projects-table td {
                padding: 10px;
            }
        }

        /* Scroll behavior */
        html {
            scroll-behavior: smooth;
        }

        /* Footer */
        footer {
            background: #333;
            color: white;
            text-align: center;
            padding: 40px 0;
            margin-top: 60px;
        }

        footer p {
            font-size: 1.1em;
            margin-bottom: 20px;
        }

        .contact-info {
            display: flex;
            justify-content: center;
            gap: 30px;
            flex-wrap: wrap;
        }

        .contact-info a {
            color: #667eea;
            text-decoration: none;
            font-weight: 500;
            transition: all 0.3s ease;
        }

        .contact-info a:hover {
            color: #764ba2;
            transform: translateY(-2px);
        }
        """

    def generate_javascript(self):
        """JavaScript 코드 생성"""
        return """
        // Smooth scrolling for navigation links
        document.querySelectorAll('nav a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });

        // Active navigation highlighting
        window.addEventListener('scroll', function() {
            const sections = document.querySelectorAll('section[id]');
            const navLinks = document.querySelectorAll('nav a');
            
            let current = '';
            sections.forEach(section => {
                const sectionTop = section.offsetTop;
                const sectionHeight = section.clientHeight;
                if (window.scrollY >= sectionTop - 200) {
                    current = section.getAttribute('id');
                }
            });

            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === `#${current}`) {
                    link.classList.add('active');
                }
            });
        });

        // Animate elements on scroll
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, observerOptions);

        // Observe all sections and timeline items
        document.querySelectorAll('.section, .timeline-item').forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(20px)';
            el.style.transition = 'all 0.6s ease-out';
            observer.observe(el);
        });

        // Table row hover effects
        document.querySelectorAll('.projects-table tr').forEach(row => {
            row.addEventListener('mouseenter', function() {
                this.style.transform = 'scale(1.02)';
                this.style.boxShadow = '0 5px 15px rgba(102, 126, 234, 0.2)';
            });
            
            row.addEventListener('mouseleave', function() {
                this.style.transform = 'scale(1)';
                this.style.boxShadow = 'none';
            });
        });
        """

    def get_timeline_data(self):
        """타임라인 데이터 정의"""
        return [
            {'period': '2015 ~ 2019', 'content': '오프라인 마케팅 / 전시·이벤트 및 고객 체험 경험 설계 중심'},
            {'period': '2020', 'content': '브랜드 체험 축소 → 온라인 전환 가속화'},
            {'period': '2021', 'content': '디지털 콘텐츠 중심 마케팅 활성화'},
            {'period': '2022', 'content': '온·오프라인 통합 (IMC)'},
            {'period': '2023 ~ 2024', 'content': '데이터 기반 전략 본격화'},
            {'period': '2025', 'content': '생성형 AI 콘텐츠 및 마테크 자동화 확산'}
        ]

    def get_career_data(self):
        """커리어 데이터 정의"""
        return [
            {'period': '초기 (2015~2016)', 'content': '전시·공간 기획 → 오프라인 접점 설계'},
            {'period': '중기 (2020~2023)', 'content': '에이전시 재직 → IMC 캠페인, 퍼포먼스 마케팅, SNS 콘텐츠, 굿즈 마케팅, 체험 프로젝트 리드'},
            {'period': '최근 (2023~2025)', 'content': '브랜드 인하우스 마케터 전환 → B2B 전략, CI/BI 정비, 세일즈킷, CRM, 디지털 채널 최적화'},
            {'period': '향후 (2025 이후)', 'content': '생성형 AI 기반 콘텐츠 자동화 및 마테크 생태계 확장 지향'}
        ]

    def get_certifications(self):
        """자격증 데이터 정의"""
        return [
            '2018년 MA 졸업 (Event & Conference Management)',
            '2022년 7월 : 검색광고마케터 1급',
            '2024년 9월 : 데이터분석 준전문가 (ADsP)',
            '2025년 5~7월 : Business 데이터분석 사외 프로젝트 수료'
        ]

    def get_swot_data(self):
        """SWOT 분석 데이터 정의"""
        return {
            'strengths': [
                '✅ 온·오프 통합 마케팅 경험',
                '✅ 글로벌/B2B 전략 기획',
                '✅ 크로스펑셔널 협업 & 커뮤니케이션',
                '✅ 다양한 사업군 프로젝트 경험'
            ],
            'opportunities': [
                '✅ AI 기반 콘텐츠 자동화',
                '✅ Cloud Native 디지털 전환 가속화',
                '✅ 하이브리드 이벤트 확장'
            ],
            'weaknesses': [
                '⚠️ 데이터 사이언스 역량 보완 필요'
            ],
            'threats': [
                '⚠️ 빠른 트렌드·기술 변화',
                '⚠️ 예산 축소 리스크'
            ]
        }

    def get_projects_data(self):
        """프로젝트 데이터 정의"""
        return [
            {
                'rank': 1,
                'skill': '전략적 브랜드 포지셔닝',
                'description': '시장·경쟁사 심층 분석으로 핵심 차별점 도출<br>장기 브랜드 아키텍처 설계·관리',
                'project': 'TmaxCloud 브랜드 전략',
                'issue': '사업 쇠퇴로 신뢰도 약화<br>포트폴리오 재포지셔닝 부재',
                'solution': '온드미디어·PR로 \'정상화 스토리\' 집중 배포<br>맞춤 콘텐츠 제작·배포로 신뢰 회복'
            },
            {
                'rank': 2,
                'skill': '소비자 인사이트 & 스토리텔링',
                'description': '정성·정량 리서치로 니즈 포착<br>감성·논리 결합 내러티브 전개',
                'project': 'Campari 홈텐딩 키트',
                'issue': '팬데믹으로 오프라인 경험 단절',
                'solution': '풀 키트 구성 & 편의점 유통 강화<br>2,000세트 완판·SNS 버즈 확대'
            },
            {
                'rank': 3,
                'skill': '통합 캠페인 기획·운영',
                'description': '온·오프 채널 연계 IMC 설계·실행<br>실시간 성과 모니터링',
                'project': 'SK TECH SUMMIT 2022',
                'issue': '온라인 참여 프로그램 미비',
                'solution': '로봇 원격 전시 투어 기획<br>사전 웨비나 & 안내 영상 배포'
            },
            {
                'rank': 4,
                'skill': '데이터 기반 퍼포먼스 최적화',
                'description': 'Owned/Paid 미디어 데이터 통합 분석<br>A/B 테스트 & 리포팅',
                'project': '어도비기너 캠페인',
                'issue': '구독 일탈 원인: 사용 편의성·시간 부담',
                'solution': '게임화 튜토리얼 개발<br>Paid 채널 1,000명 참여 달성'
            },
            {
                'rank': 5,
                'skill': '디지털 혁신 & 기술 활용',
                'description': 'Python·SQL·Streamlit 대시보드 개발<br>AI 개인화 추천 시스템',
                'project': '제주 감귤 사외 프로젝트',
                'issue': '재배지 정보 부재로 의사결정 어려움',
                'solution': 'ETL & 대시보드 구축<br>최적 재배지 추천 기능 제공'
            },
            {
                'rank': 6,
                'skill': '브랜드 아이덴티티 관리',
                'description': 'CI/BI 가이드라인 수립 & 업데이트<br>자산 관리 프로세스 정립',
                'project': 'Wemade CI/BI 리뉴얼',
                'issue': '혼재된 메시지·에셋 사용으로 분산',
                'solution': '구글 드라이브 자산화 & 검수 프로세스 도입<br>매뉴얼·사례집 제작'
            },
            {
                'rank': 7,
                'skill': '커뮤니케이션 & 협업 역량',
                'description': '맞춤 커뮤니케이션 프로토콜 구축<br>크로스펑셔널 협업',
                'project': 'Wemade 글로벌 행사',
                'issue': '파트너 간 의사소통 이슈',
                'solution': '영문 이메일 & 콜컨퍼런스 운영<br>브릿지 역할 수행'
            },
            {
                'rank': 8,
                'skill': '콘텐츠 전략 & 카피라이팅',
                'description': '채널별 톤앤매너 개발<br>UTM·GA4 연동 성과 분석',
                'project': 'TmaxCloud 채널 콘텐츠',
                'issue': '획일적 게시로 반응 저조',
                'solution': '포맷 최적화 & 계정 체계화<br>UTM/GA4 분석으로 전환율 2배↑'
            }
        ]

    def generate_html(self):
        """HTML 포트폴리오 생성"""
        timeline_data = self.get_timeline_data()
        career_data = self.get_career_data()
        certifications = self.get_certifications()
        swot_data = self.get_swot_data()
        projects_data = self.get_projects_data()
        
        html_content = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.portfolio_data['name']} | {self.portfolio_data['title']}</title>
    <style>
        {self.generate_css()}
    </style>
</head>
<body>
    <!-- Navigation -->
    <nav>
        <ul>
            <li><a href="#home" class="active">Home</a></li>
            <li><a href="#overview">Overview</a></li>
            <li><a href="#analysis">Market Analysis</a></li>
            <li><a href="#projects">Projects</a></li>
        </ul>
    </nav>

    <div class="container">
        <!-- Hero Section -->
        <section id="home" class="hero">
            <h1>{self.portfolio_data['name']}</h1>
            <p class="subtitle">{self.portfolio_data['subtitle']}</p>
            <div class="keywords">
                {''.join([f'<p><strong>{keyword}</strong></p>' for keyword in self.portfolio_data['keywords']])}
            </div>
        </section>

        <!-- Overview Section -->
        <section id="overview" class="section">
            <h2>▶️ 개요</h2>
            <h3>제안 목적</h3>
            <p>브랜드 마케팅 조직에 전략적 성장을 제안하는 인재 QKR진희 소개</p>

            <h3>핵심 메시지</h3>
            <p><strong>기획-실행-분석</strong>을 아우르는 통합형 마케팅 역량</p>

            <div class="triangle-container">
                <div class="triangle">
                    🧠 전략 기획<br>
                    /&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\\<br>
                    /&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\\<br>
                    ⚙️ 실행력 ────── 📊 데이터 분석
                </div>
            </div>
        </section>

        <!-- Market Analysis Section -->
        <section id="analysis" class="section">
            <h2>▶️ 시장 환경 및 배경 분석</h2>
            <p style="text-align: center; font-size: 1.2em; color: #764ba2; margin-bottom: 40px;">
                "트렌드 위에 기획하고, 흐름 안에 실행한 브랜드 마케터, 박진희 여정"
            </p>

            <h3>1. 마케팅 산업의 흐름 (2015~2025)</h3>
            <div class="timeline">
                {''.join([f'''
                <div class="timeline-item">
                    <strong>{item["period"]}</strong><br>
                    {item["content"]}
                </div>''' for item in timeline_data])}
            </div>

            <h3>2. 진희의 커리어 역량 진화</h3>
            <div class="timeline">
                {''.join([f'''
                <div class="timeline-item">
                    <strong>{item["period"]}</strong><br>
                    {item["content"]}
                </div>''' for item in career_data])}
            </div>

            <h3>자격증 및 교육</h3>
            <div style="background: #f8f9ff; padding: 30px; border-radius: 15px; margin: 30px 0;">
                <ul style="list-style: none; padding: 0;">
                    {''.join([f'<li style="margin: 10px 0;">• {cert}</li>' for cert in certifications])}
                </ul>
            </div>

            <h3>3. SWOT 분석</h3>
            <div class="swot-grid">
                <div class="swot-card">
                    <h4>강점 (Strengths)</h4>
                    <ul>
                        {''.join([f'<li>{item}</li>' for item in swot_data['strengths']])}
                    </ul>
                </div>
                <div class="swot-card">
                    <h4>기회 (Opportunities)</h4>
                    <ul>
                        {''.join([f'<li>{item}</li>' for item in swot_data['opportunities']])}
                    </ul>
                </div>
                <div class="swot-card">
                    <h4>약점 (Weaknesses)</h4>
                    <ul>
                        {''.join([f'<li>{item}</li>' for item in swot_data['weaknesses']])}
                    </ul>
                </div>
                <div class="swot-card">
                    <h4>위협 (Threats)</h4>
                    <ul>
                        {''.join([f'<li>{item}</li>' for item in swot_data['threats']])}
                    </ul>
                </div>
            </div>
        </section>

        <!-- Projects Section -->
        <section id="projects" class="section">
            <h2>▶️ 프로젝트 분석 : 이슈 및 대응</h2>
            <table class="projects-table">
                <thead>
                    <tr>
                        <th>순위</th>
                        <th>역량 명칭</th>
                        <th>설명 및 어필 포인트</th>
                        <th>프로젝트</th>
                        <th>이슈</th>
                        <th>대응</th>
                    </tr>
                </thead>
                <tbody>
                    {''.join([f'''
                    <tr>
                        <td><div class="rank-badge">{project["rank"]}</div></td>
                        <td><strong>{project["skill"]}</strong></td>
                        <td>{project["description"]}</td>
                        <td>{project["project"]}</td>
                        <td>{project["issue"]}</td>
                        <td>{project["solution"]}</td>
                    </tr>''' for project in projects_data])}
                </tbody>
            </table>
        </section>
    </div>

    <!-- Footer -->
    <footer>
        <p>Ready to make an impact together?</p>
        <div class="contact-info">
            <a href="mailto:{self.portfolio_data['contact']['email']}">📧 Contact Me</a>
            <a href="tel:{self.portfolio_data['contact']['phone']}">📞 Call Me</a>
            <a href="{self.portfolio_data['contact']['linkedin']}" target="_blank">💼 LinkedIn</a>
        </div>
    </footer>

    <script>
        {self.generate_javascript()}
    </script>
</body>
</html>"""
        return html_content

    def save_portfolio(self, filename='portfolio.html'):
        """포트폴리오 HTML 파일 저장"""
        html_content = self.generate_html()
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html_content)
            print(f"✅ 포트폴리오가 성공적으로 생성되었습니다: {filename}")
            print(f"📁 파일 위치: {os.path.abspath(filename)}")
            return True
        except Exception as e:
            print(f"❌ 파일 생성 중 오류가 발생했습니다: {e}")
            return False

    def create_project_folder(self, folder_name='jinhee_portfolio'):
        """프로젝트 폴더 생성 및 파일들 저장"""
        try:
            # 폴더 생성
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
                print(f"📁 폴더 생성: {folder_name}")
            
            # HTML 파일 저장
            html_path = os.path.join(folder_name, 'index.html')
            if self.save_portfolio(html_path):
                print(f"🌐 브라우저에서 확인: file://{os.path.abspath(html_path)}")
                
            return True
        except Exception as e:
            print(f"❌ 프로젝트 폴더 생성 중 오류: {e}")
            return False


def main():
    """메인 실행 함수"""
    print("🚀 Jinhee Park 포트폴리오 생성기를 시작합니다...")
    
    # 포트폴리오 생성기 인스턴스 생성
    generator = PortfolioGenerator()
    
    # 프로젝트 폴더 생성 및 파일 저장
    if generator.create_project_folder():
        print("\n🎉 포트폴리오 생성이 완료되었습니다!")
        print("📖 사용법:")
        print("   1. 생성된 index.html 파일을 브라우저에서 열기")
        print("   2. 연락처 정보 수정 (line 15-19)")
        print("   3. 프로젝트 데이터 추가/수정 (line 280-350)")
        print("   4. GitHub Pages나 Netlify에 배포")
    else:
        print("❌ 포트폴리오 생성에 실패했습니다.")


if __name__ == "__main__":
    main()
