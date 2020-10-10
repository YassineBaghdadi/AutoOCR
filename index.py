import time

import os, sys, random
from PyQt5 import QtWidgets, uic
from time import strftime
from time import gmtime
import platform
DESKTOP = os.path.join(os.path.join(os.environ['USERPROFILE']),'Desktop') if platform.system() == 'Windows' else os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')


class Counter(QtWidgets.QWidget):
    def __init__(self):
        super(Counter, self).__init__()
        uic.loadUi(os.path.join(os.path.dirname(__file__), 'counter.ui'), self)

        self.started = False
        self.start.clicked.connect(self.start_)

    def closeEvent(self, event):
        try:
            self.m.close()
        except:
            pass
        self.close()

    def start_(self):
        if self.started:
            self.end = time.time()
            self.start.setText('START')
            score = self.m.calc()
            self.err.setText(f'ERRORS : {str(24 - score)}, ACCURACY : {(score/24)*100}%')

            # self.m.close()
            self.started = False
            time_ = strftime("%H:%M:%S", gmtime(self.end - self.startTime))
            self.co.setText(f'Time : {time_}')
            
            if not os.path.exists(os.path.join(DESKTOP, 'training')):
                os.makedirs(os.path.join(DESKTOP, 'training'))
            with open(os.path.join(DESKTOP, 'training', 'logs.txt'), 'a') as f:
                f.write(f'{str(strftime(f"%d-%m-%Y %H:%M:%S", gmtime()))}  -- >  Time : {time_}, Errors : {str(24 - score)}, Accuracy : {(score/24)*100}%\n')
                """
            with open('logs.txt', 'a') as f:
                f.write(f'{str(strftime(f"%d-%m-%Y %H:%M:%S", gmtime()))}  -- >  Time : {time_}, Errors : {str(24 - score)}, Accuracy : {(score/24)*100}%\n')
                """
        else:
            self.startTime = time.time()


            self.start.setText('STOP')
            self.m = Main()

            self.setFixedSize(QtWidgets.QDesktopWidget().screenGeometry(-1).width(), 100)
            self.move(0, 0)
            self.m.close()
            self.m.show()
            self.m.setFixedWidth(QtWidgets.QDesktopWidget().screenGeometry(-1).width())
            self.m.move(0, 200)
            self.started = True




class Main(QtWidgets.QWidget):
    def __init__(self):
        super(Main, self).__init__()
        uic.loadUi(os.path.join(os.path.dirname(__file__), 'ui.ui'), self)
        self.score = 0
        self.names = ['Ba Jin', 'Baab Heinrich', 'Báb', 'Baba Meher', 'Baba Tupeni',
        'Babaji Haidakhan', 'Babauta Leo', 'Babbage Charles', 'Babbitt Irving', 'Babbitt Milton',
        'Babinet Jacques', 'Baboulene David', 'Babur', 'Baca Jimmy Santiago', 'Baca Judy', 'Bacall Lauren',
        'Bacevich Andrew', 'Bach Carl Philipp Emanuel', 'Bach Erich von dem', 'Bach Johann Sebastian', 'Bach Richard',
        'Bach Sebastian', 'Bacharach Burt', 'Bachchan Amitabh', 'Bachelard Gaston', 'Bachelot Roselyne', 'Bachmann Michele', 'Bacigalupi Paolo', 'Backhaus Wilhelm', 'Backus John', 'Bacon Francis', 'Bacon Francis (artist)', 'Bacon Leonard', 'Bacon Roger', 'Badawi Abdullah Ahmad', 'Baddiel David', 'Baden-Powell Sir Robert (B-P)', 'Bader Douglas', 'Badian Ernst', 'Badiou Alain', 'Badnarik Michael', 'Badoglio Pietro', 'Badu Erykah', 'Baedeker Karl', 'Baez Joan', 'Bagehot Walter', 'Baggio Roberto', 'Baggott Jim', 'Bagramyan Hovhannes', "Bahá'u'lláh", 'Bahcall John N.', 'Bai–Bam', 'Bai Chongxi', 'Bai Jushan', 'Bai Meera', 'Bailey Alice', 'Bailey Bill', 'Bailey F. Lee', 'Bailey Pearl', 'Bailey Philip James', 'Bailey Thomas A.', 'Bailey Trevor', 'Baillie Bruce', 'Baillie Joanna', 'Bailyn Bernard', 'Bain Alexander', 'Bainbridge Beryl', 'Bainimarama Frank', 'Bairaktaris Porphyrios', 'Baird Diora', 'Bak Per', 'Bakan Joel', 'Baker General', 'Baker Jack', 'Baker James', 'Baker Kage', 'Baker Mitchell', 'Baker Russell', 'Baker Stewart', 'Baker Tom', 'Bakewell Sarah', 'Bakhtiari Marjaney', 'Bakker R. Scott', 'Bakr Abu', 'Bakri Omar', 'Bakshi Ralph', 'Bakunin Mikhail', 'Bala', 'Balamuralikrishna M.', 'Balasaraswati', 'Balašević Đorđe', 'Balcer Rene', 'Balcon Michael', 'Balder Artur', 'Baldinucci Filippo', 'Baldwin Alec', 'Baldwin James', 'Baldwin Roger Nash', 'Baldwin Stanley', 'Balestrero Gregory', 'Balfour Arthur', 'Balfour Francis Maitland', 'Balko Radley', 'Ball Hugo', 'Ball John (priest)', 'Ball Lucille', 'Ball Robert Stawell', 'Balla Giacomo', 'Ballard J. G.', 'Balliett Whitney', 'Ballou Adin', 'Ballou Hosea', 'Balsekar Ramesh', 'Balsillie Jim', 'Balzac Honoré de', 'Balzac Jean-Louis Guez de Balzac', 'Bambaataa Afrika', 'Bamford Maria', 'Ban–Barn', 'Ban Ki-moon', 'Bancroft Anne', 'Bancroft George', 'Banda Hastings', 'Bandeira Manuel', 'Bandura Albert', 'Bang Abhay', 'Banglie Lu', 'Bangs Edward', 'Bangs John Kendrick', 'Bangs Lester', 'Banhart Devendra', 'Bankhead Tallulah', 'Banks Ernie', 'Banks Iain', 'Banks Joseph', 'Banks Robert', 'Banks Tony (Lord Stratford)', 'Banks Tyra', 'Banksy', 'Banna Hassan', 'Banneker Benjamin', 'Bannerman Frances', 'Bannister Roger', 'Banville John', 'Bara Theda', 'Barak Ehud', 'Baraka Amiri', 'Baran Paul A.', 'Barassi Ron', 'Barât Carl', 'Baratynsky Evgeny', 'Barbaccia Gregory', 'Barbara (singer)', 'Barbauld Anna Letitia', 'Barbeau Adrienne', 'Barber Benjamin', 'Barber Margaret', 'Barberi Gina', 'Barbie Klaus', 'Barbour John', 'Barbusse Henri', 'Barbut James', 'Barclay Robert', 'Barclay William', 'Bardeen John', 'Bardon Franz', 'Bardot Brigitte', 'Bareilles Sara', 'Barenboim Daniel', 'Barère de Vieuzac Bertrand',
        'Barham Richard Harris', 'Baring Evelyn 1st Earl of Cromer', 'Baring Maurice', 'Baring-Gould Sabine', 'Barker Clive', 'Barker George', 'Barker Jane', 'Barker Nicola', 'Barkley Charles', 'Barlas John Evelyn', 'Barlow George', 'Barlow Harold', 'Barlow Joel', 'Barlow John Perry', 'Barlow Peter (mathematician)', 'Barnard Chester', 'Barnes Albert', 'Barnes Djuna', 'Barnes John', 'Barnes Julian', 'Barnes Kevin', 'Barnes Roy', 'Barnes Simon', 'Barnes William', 'Barnette Henlee Hulix', 'Barney Matthew', 'Barney Natalie Clifford', 'Barnfield Richard', 'Barnhill John Basil', 'Barnum P. T.', 'Baro–Baz', 'Baron Alexander', 'Barr Alfred', 'Barr Bob', 'Barr James', 'Barr Matthias', 'Barr Nicholas', 'Barr Robert', 'Barr Stringfellow', 'Barragán Luis', 'Barraza Santa', 'Barrett James Lee', 'Barre Siad', 'Barreto Lima', 'Barrett Michael', 'Barrett William (philosopher)', 'Barrett Syd', 'Barrie J. M.', 'Barrington George', 'Barro Robert', 'Barron Charles', 'Barron Carl', 'Barrow Isaac', 'Barrowman John', 'Barry Dave', 'Barry Kevin', 'Barry Marion', 'Barry Max', 'Barry Michael Joseph', 'Barry Robert', 'Barry Todd', 'Barrymore John', 'Barsky Vladimir', 'Bart Lionel', 'Barth Alan', 'Barth John', 'Barth Karl', 'Bartholomew of San Concordio', 'Barthelme Donald', 'Barthes Roland', 'Bartle Richard', 'Bartlett Bruce Reeves', 'Bartlett Charles L. (journalist)', 'Bartók Béla', 'Barton Bruce Fairchild', 'Barton Joe', 'Barton Joey', 'Baruch Bernard', 'Barwich Heinz', 'Baryshnikov Mikhail', 'Barzani Massoud', 'Barzun Jacques', 'Basava', 'Bascom John', 'Bashford Henry Howarth', 'Bashir Abu Bakar', 'Bashir Omar', 'Bashō Matsuo', 'Basie Count', 'Baskin Leonard', 'Basquiat Jean-Michel', 'Bass Kyle', 'Bassani Franco', 'Bastami Bayazid', "Bastard Ol' Dirty", 'Bastard Thomas', 'Bastiat Frédéric', 'Baťa Tomáš', 'Bataille Georges', 'Batalvi Shiv Kumar', 'Bates Brian (psychologist)', 'Bates Marston', 'Bateson Gregory', 'Bateson Thomas', 'Bateson William', 'Bath Elizabeth', 'Bathgate Andy', 'Batistuta Gabriel', 'Battcock Gregory', 'Battelle John', 'Battuta Ibn', 'Bauby Jean-Dominique', 'Baude Frank', 'Baudelaire Charles', 'Baudrillard Jean', 'Bauer Bruno', 'Bauer Erich', 'Bauer Friedrich', 'Bauer Marion', 'Bauer Yehuda', 'Baum L. Frank', 'Bauman Neil', 'Bauman Zygmunt', 'Bavadra Timoci', 'Bax Ernest Belfort', 'Baxter J. Sidlow', 'Baxter Richard', 'Baxter Stephen', 'Bayeza Ifa', 'Bayle Pierre', 'Bayley Sir John 1st Baronet', 'Baylis Trevor', 'Bayly Thomas Haynes', 'Baziotes William', 'Bea–Bel', 'Beachcomber', 'Beadle George', 'Beagle Peter S.', 'Beals Jennifer', 'Bear Greg', 'Beard Charles A.', 'Beard Henry', 'Beard Peter', 'Beardsley Aubrey', 'Beattie James', 'Beattie Peter',
        'Beatty David 1st Earl Beatty', 'Beaumarchais Pierre', 'Beaumont Francis', 'Princess Beatrice of the United Kingdom', 'Beaverbrook 1st Baron', 'Bechdel Alison', 'Beck', 'Beck Aaron', 'Beck Charlie', 'Beck Glenn', 'Beck Guido', 'Beck Jeff', 'Beck Kent', 'Beck Martin', 'Becker Carl L.', 'Becker Ernest', 'Becker Gary', 'Beckett Samuel', 'Beckett Wendy', 'Beckford Peter', 'Beckford William Thomas', 'Beckham David', 'Beckham Victoria', 'Beckinsale Kate', 'Beckmann Max', 'Becon Thomas', 'Beddoes Thomas Lovell', 'Beddome Richard Henry', 'Bede', 'Bedi Protima', 'Bedingfield Natasha', 'Beebe William', 'Beecham Thomas', 'Beecher Henry Ward', 'Beeching Henry Charles', 'Beefheart Captain', 'Beenakker Carlo', 'Beeley Vanessa', 'Beer Anthony Stafford', 'Beer Arthur', 'Beerbohm Max', 'Beers Ethel Lynn', 'Beethoven Ludwig van', 'Begala Paul', 'Begin Menachem', 'Behan Brendan', 'Behar Joy', 'Behar Richard', 'Beharry Johnson', 'Behe Michael', 'Behn Aphra', 'Behramoğlu Ataol', 'Beilin Yossi', 'Belafonte Harry', 'Belisarius', 'Bell Alexander Graham', 'Bell Daniel', 'Bell Gordon', 'Bell John Stewart', 'Bell Kristen', 'Bell Marvin', 'Bellah Robert', 'Bellamy Edward', 'Belle David', 'Bellegarrigue Anselme', 'Beller Mara', 'Belloc Hilaire', 'Bellow Saul', 'Bellucci Monica', 'Belpré Pura', 'Belushi Jim', 'Belushi John', 'Ben–Berk', 'Benchley Robert', 'Benda Julien', 'Benedict of Nursia', 'Benedict XV Pope', 'Benedict XVI (Pope)', 'Benenson Peter', 'Benét Stephen Vincent', 'Benford Gregory', 'Benger Elizabeth', 'Ben-Gurion David', 'Benioff Marc', 'Benítez Rafael', 'Benjamin Judah P.', 'Benjamin Park Sr.', 'Benjamin Walter', 'Benkin Richard', 'Benn Nigel', 'Benn Tony', 'Bennett Alan', 'Bennett Arnold', 'Bennett Billy', 'Bennett Bruce', 'Bennett Tony', 'Benning Henry Lewis', 'Bennis Warren', 'Benny Jack', 'Benserade Isaac de', 'Benson A. C.', 'Benson Amber', 'Benson E. F.', 'Benson Ezra Taft', 'Benson George', 'Bentham Jeremy', 'Bentley Edmund Clerihew', 'Bentley Elizabeth', 'Bentley Richard', 'Bentsen Lloyd', 'Benzine Craig', 'Berardinelli James', 'Bercovitch Sacvan', 'Berays Edward', 'Berdimuhammedov Gurbanguly', 'Berdyaev Nikolai', 'Béranger Pierre-Jean de', 'Berenson Bernard', 'Beresford Lord Charles', 'Berezovsky Boris', 'Berg Alban', 'Bergdahl Bowe', 'Bergen Edgar', 'Berger John', 'Berger Ric', 'Berger Sandy', 'Bergerac Cyrano de', 'Bergland Richard', 'Bergkamp Dennis', 'Bergman Ingmar', 'Bergman Ingrid', 'Bergson Henri-Louis', 'Beria Lavrentiy', 'Berio Luciano', 'Berisha Sali', 'Berkeley George', 'Berkman Alexander', 'Berkofsky Martin', 'Berkovic Eyal', 'Berl–Bez', 'Berle Milton', 'Berleant Arnold', 'Berlet Chip', 'Berlin Irving', 'Berlin Isaiah',
        'Berlinerblau Jacques', 'Berlinski Claire', 'Berlioz Hector', 'Berlusconi Silvio', 'Berman Boris', 'Berman Chris', 'Berman Russell', 'Bern Dan', 'Bernadotte Folke', 'Bernal John Desmond', 'Bernanke Ben', 'Bernanos Georges', 'Bernard of Clairvaux', 'Bernard Claude', 'Bernard Jeffrey', 'Bernart de Ventadorn', 'Bernays Paul', 'Berne Eric', 'Berners-Lee Tim', 'Bernhard Sandra', 'Bernhardt Sarah', 'Berni Francesco', 'Bernis François-Joachim de Pierre de', 'Bernoulli Daniel', 'Bernstein Andrew', 'Bernstein Carl', 'Bernstein Charles', 'Bernstein Daniel J.', 'Bernstein Eduard', 'Bernstein Jared', 'Bernstein Jeremy', 'Bernstein Leonard', 'Bernus Peter', 'Beron Petar', 'Berra Yogi', 'Berridge John', 'Berrigan Daniel', 'Berrigan Philip', 'Berry Chuck', 'Berry Halle', 'Berry Paul', 'Berry Scyld', 'Berry Siân', 'Berry Wendell', 'Berryman Guy', 'Bertin Jacques', 'Bertoletti Leon', 'Besant Annie', 'Besant Walter', 'Besset Timothee', 'Besson Luc', 'Best George', 'Bester Alfred', 'Beston Henry', 'Betancourt Íngrid', 'Beteille Andre', 'Bethe Hans', 'Bethune George Washington', 'Betjeman John', 'Bettany Paul', 'Bettis Hilary', 'Bettis Jerome', 'Betts Reginald', 'Beuys Joseph', 'Bevan Aneurin', 'Beveridge William Henry 1st Baron Beveridge of Tuggal', 'Beveridge William Ian Beardmore', 'Bevin Ernest', 'Bezalel Judah Loew ben', 'Bezos Jeff', 'Bh–Bi', 'Bhabha Homi J.', 'Bhagat Chetan', 'Bhagwandas Rana', 'Bhagwat Mohan', 'Bharathi Subramanya', 'Bhatt Ela', 'Bhutto Benazir', 'Bhutto Zulfikar Ali', 'Biafra Jello', 'Bias of Priene', 'Bibesco Princess Elizabeth', 'Bichat Marie François Xavier', 'Bickerstaffe Isaac', 'Bickersteth Edward (bishop of Exeter)', 'Bickersteth Henry 1st Baron Langdale', 'Bickerton A.W.', 'Bickle Mike', 'Bidault Georges', 'Biden Joseph ("Joe")', 'Bieber Justin', 'Biel Gabriel', 'Bierce Ambrose', 'Big L (rapper)', 'Bigg John Stanyan', 'Biggs Jason', 'Bilbo Theodore G.',
        'Bilić Slaven', 'Billig Michael', 'Billings Josh', 'Billy the Kid', 'Binchy Maeve', 'Binet Hélène', 'Bingham Thomas Baron Bingham of Cornhill', 'Binkley Thomas', 'Binnig Gerd', 'Binoche Juliette', 'Binyon Laurence', 'Bion of Borysthenes', 'Biot Jean-Baptiste', 'Bird Brad', 'Bird Larry', 'Bird Mary Brave', 'Birdman (entertainer)', 'Birgeneau Robert J.', 'Biriuzov Sergei', 'Birkett William Norman  1st Baron Birkett', 'Birrell Augustine', 'Birtwistle Harrison', 'Bīrūnī Abū-Rayhān', 'Bishop Elizabeth', 'Bishop Isabel', 'Bishop Jim', 'Bishop Michael', 'Bismarck Otto von', 'Bittencourt de Oliveira Simone', 'Bittrich Wilhelm', 'Bixler-Zavala Cedric', 'Bizet Georges', 'Bl', 'Blaauw Gerrit', 'Blacc Aloe', 'Black Elk', 'Black Bob', 'Black Conrad', 'Black Hugo', 'Black Jack', 'Black Joseph', 'Black Lewis', 'Blackburn Colin Baron Blackburn', 'Blackburn Olly', 'Blackburn Simon', 'Blacker Valentine', 'Blacker William', 'Blackie John Stuart', 'Blackmore Richard', 'Blackmore Ritchie', 'Blackmore Susan', 'Blackmun Harry', 'Blackstone William', 'Blackwell Nigel', 'Blackwood Helen Baroness Dufferin and Claneboye', 'Blackwood Richard', 'Blades Rubén', 'Blagojevich Rod', 'Blaine David', 'Blaine James G.', 'Blair Cherie', 'Blair Hugh', 'Blair Robert', 'Blair Tony', 'Blake James', 'Blake Kendare', 'Blake Peter', 'Blake William', 'Blakemore Colin', 'Blakey Art', 'Blalock Jolene', 'Blanc Raymond', 'Blanchard Olivier', 'Blanchard Samuel Laman', 'Blanchett Cate', 'Blanchflower David', 'Blanco Cuauhtémoc', 'Blanco Richard', 'Blandy William H. P.', 'Blatchford Robert', 'Blavatsky Helena Petrovna', 'Blears Hazel', 'Bledel Alexis', 'Bleecker Ann Eliza', 'Bleibtreu-Ehrenberg Gisela', 'Bleu Corbin', 'Blinder Alan', 'Blish James', 'Blix Hans', 'Blixen Karen', 'Blobel Paul', 'Bloch Ernst', 'Bloch Felix', 'Blodget Henry', 'Bloembergen Nicolaas', 'Blok Alexander', 'Blom Eric', 'Blomberg Werner von', 'Blond Phillip', 'Bloom Allan', 'Bloom Godfrey', 'Bloom Harold', 'Bloom Howard', 'Bloom Orlando', 'Bloom Paul', 'Bloomberg Michael', 'Bloomfield Robert', 'Blount Roy', 'Blow Charles McRay', 'Blu (rapper)', 'Blum William', 'Blume Judy', 'Blumenauer Earl', 'Blunden Edmund Charles', 'Blunt James', 'Blunt Wilfrid Scawen', 'Bly Robert W.', 'Blyleven Bert', 'Blythe Randy', 'Boa–Boo', 'Boal Augusto', 'Boardman George the Younger', 'Boarman Charles', 'Boas Franz', 'Boateng Kevin-Prince', 'Boaz David', 'Bobbio Norberto', 'Boccaccio Giovanni', 'Boccioni Umberto', 'Bochner Mel', 'Boe Christoffer', 'Boehm Barry', 'Boehner John', 'Boesky Ivan', 'Boethius Anicius Manlius Severinus', 'Bogart Humphrey', 'Bogart Neil', 'Bogdanov Alexander', 'Boggs Hale', 'Bogle John', 'Bohlin Nils']
        self.chars = [ str(i) for i in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!'\"£$%&*()_-+=|/?>,<#~@;:1234567890"]

        self.v1 = random.choice(self.names)
        self.v2 = f'{self.v1.upper()[0]}.{self.v1.upper().split(" ")[1][0]}.'
        self.v3 = f'{".".join(self.v1.lower().split(" "))}@{random.choice(list("gmail mail icloud protonmail fastmail fakemail justmail 4mail urmail testmail".split(" ")))}.{random.choice("com net fr me ma tk ru us test".split(" "))}'
        self.v4 = ''.join(list(random.choices(self.chars, k=6)))
        self.v5 =''.join(random.choices(self.chars, k=7))
        self.v6 =''.join(random.choices(self.chars, k=11))
        self.v7 =''.join(random.choices(self.chars, k=19))
        self.v8 =''.join(random.choices(self.chars, k=7))
        self.v9 =''.join(random.choices(self.chars, k=15))
        self.v10 =''.join(random.choices(self.chars, k=16))
        self.v11 =''.join(random.choices(self.chars, k=18))
        self.v12 =''.join(random.choices(self.chars, k=10))
        self.v13 =''.join(random.choices(self.chars, k=6))
        self.v14 = ''.join(random.choices(self.chars, k=9))
        self.v15 = ''.join(random.choices(self.chars, k=14))
        self.v16 = ''.join(random.choices(self.chars, k=8))
        self.v17 = ''.join(random.choices(self.chars, k=9))
        self.v18=''.join(random.choices(self.chars, k=6))
        self.v19 =''.join(random.choices(self.chars, k=9))
        self.v20  =''.join(random.choices(self.chars, k=6))
        self.v21 = ''.join(random.choices(self.chars, k=6))
        self.v22=''.join(random.choices(self.chars, k=6))
        self.v23 =''.join(random.choices(self.chars, k=9))
        self.v24 = ''.join(random.choices(self.chars, k=6))
        self.l1.setText(self.v1)
        self.l2.setText(self.v2)
        self.l3.setText(self.v3)
        self.l4.setText(self.v4)
        self.l5.setText(self.v5)
        self.l6.setText(self.v6)
        self.l7.setText(self.v7)
        self.l8.setText(self.v8)
        self.l9.setText(self.v9)
        self.l10.setText(self.v10)
        self.l11.setText(self.v11)
        self.l12.setText(self.v12)
        self.l13.setText(self.v13)
        self.l14.setText(self.v14)
        self.l15.setText(self.v15)
        self.l16.setText(self.v16)
        self.l17.setText(self.v17)
        self.l18.setText(self.v18)
        self.l19.setText(self.v19)
        self.l20.setText(self.v20)
        self.l21.setText(self.v21)
        self.l22.setText(self.v22)
        self.l23.setText(self.v23)
        self.l24.setText(self.v24)
        # self.info.setText(f"""
        #     {self.v1}    {self.v2}    {self.v3}    {self.v4}    {self.v5}    {self.v6}    {self.v7}    {self.v8}    {self.v9}   {self.v10}   {self.v11}   {self.v12}     {self.v13}    {self.v14}    {self.v15}    {self.v16}    {self.v17}    {self.v18}    {self.v19}    {self.v20}    {self.v21}   {self.v22}   {self.v23}   {self.v24}
        # """)

    def calc(self):
        if self.c1.text()  == self.v1:
            self.score += 1
        else:
            self.c1.setStyleSheet('border: 2px solid red;')
            self.l1.setStyleSheet('border: 2px solid red;')
        if self.c2.text()  == self.v2 :
            self.score += 1
        else:
            self.c2.setStyleSheet('border: 2px solid red;')
            self.l2.setStyleSheet('border: 2px solid red;')
        if self.c3.text()  == self.v3 :
            self.score += 1
        else:
            self.c3.setStyleSheet('border: 2px solid red;')
            self.l3.setStyleSheet('border: 2px solid red;')
        if self.c4.text()  == self.v4:
            self.score += 1
        else:
            self.c4.setStyleSheet('border: 2px solid red;')
            self.l4.setStyleSheet('border: 2px solid red;')
        if self.c5.text() == self.v5 :
            self.score += 1
        else:
            self.c5.setStyleSheet('border: 2px solid red;')
            self.l5.setStyleSheet('border: 2px solid red;')
        if self.c6.text()  == self.v6 :
            self.score += 1
        else:
            self.c6.setStyleSheet('border: 2px solid red;')
            self.l6.setStyleSheet('border: 2px solid red;')
        if self.c7.text()  == self.v7 :
            self.score += 1
        else:
            self.c7.setStyleSheet('border: 2px solid red;')
            self.l7.setStyleSheet('border: 2px solid red;')
        if self.c8.text()  == self.v8 :
            self.score += 1
        else:
            self.c8.setStyleSheet('border: 2px solid red;')
            self.l8.setStyleSheet('border: 2px solid red;')
        if self.c9.text()  == self.v9 :
            self.score += 1
        else:
            self.c9.setStyleSheet('border: 2px solid red;')
            self.l9.setStyleSheet('border: 2px solid red;')
        if self.c10.text()  == self.v10 :
            self.score += 1
        else:
            self.c10.setStyleSheet('border: 2px solid red;')
            self.l10.setStyleSheet('border: 2px solid red;')
        if self.c11.text()  == self.v11 :
            self.score += 1
        else:
            self.c11.setStyleSheet('border: 2px solid red;')
            self.l11.setStyleSheet('border: 2px solid red;')
        if self.c12.text()  == self.v12 :
            self.score += 1
        else:
            self.c12.setStyleSheet('border: 2px solid red;')
            self.l12.setStyleSheet('border: 2px solid red;')
        if self.c13.text()  == self.v13 :
            self.score += 1
        else:
            self.c13.setStyleSheet('border: 2px solid red;')
            self.l13.setStyleSheet('border: 2px solid red;')
        if self.c14.text()  == self.v14 :
            self.score += 1
        else:
            self.c14.setStyleSheet('border: 2px solid red;')
            self.l14.setStyleSheet('border: 2px solid red;')
        if self.c15.text()  == self.v15 :
            self.score += 1
        else:
            self.c15.setStyleSheet('border: 2px solid red;')
            self.l15.setStyleSheet('border: 2px solid red;')
        if self.c16.text()  == self.v16 :
            self.score += 1
        else:
            self.c16.setStyleSheet('border: 2px solid red;')
            self.l16.setStyleSheet('border: 2px solid red;')
        if self.c17.text()  == self.v17:
            self.score += 1
        else:
            self.c17.setStyleSheet('border: 2px solid red;')
            self.l17.setStyleSheet('border: 2px solid red;')
        if self.c18.text() == self.v18 :
            self.score += 1
        else:
            self.c18.setStyleSheet('border: 2px solid red;')
            self.l18.setStyleSheet('border: 2px solid red;')
        if self.c19.text()  == self.v19 :
            self.score += 1
        else:
            self.c19.setStyleSheet('border: 2px solid red;')
            self.l19.setStyleSheet('border: 2px solid red;')
        if self.c20.text()  == self.v20 :
            self.score += 1
        else:
            self.c20.setStyleSheet('border: 2px solid red;')
            self.l20.setStyleSheet('border: 2px solid red;')
        if self.c21.text()  == self.v21 :
            self.score += 1
        else:
            self.c21.setStyleSheet('border: 2px solid red;')
            self.l21.setStyleSheet('border: 2px solid red;')
        if self.c22.text()  == self.v22 :
            self.score += 1
        else:
            self.c22.setStyleSheet('border: 2px solid red;')
            self.l22.setStyleSheet('border: 2px solid red;')
        if self.c23.text()  == self.v23 :
            self.score += 1
        else:
            self.c23.setStyleSheet('border: 2px solid red;')
            self.l23.setStyleSheet('border: 2px solid red;')
        if self.c24.text()  == self.v24 :
            self.score += 1
        else:
            self.c24.setStyleSheet('border: 2px solid red;')
            self.l24.setStyleSheet('border: 2px solid red;')

        return self.score

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    counter = Counter()
    counter.show()
    app.exec()
