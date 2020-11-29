LETRAS = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

def traduciMensaje(clave, msg, mode):
    translated = [] # stores the encrypted/decrypted msg string

    indice = 0
    clave = clave.upper()

    for char in msg: 
        num = LETRAS.find(char.upper())
        if num != -1:
            if mode == 'e':
                num += LETRAS.find(clave[indice]) 
            elif mode == 'd':
                num -= LETRAS.find(clave[indice]) 
            num %= len(LETRAS)

            if char.isupper():
                translated.append(LETRAS[num])
            elif char.islower():
                translated.append(LETRAS[num].lower())

            indice += 1 
            if indice == len(clave):
                indice = 0
        else:
            translated.append(char)

    return ''.join(translated)

encriptado = traduciMensaje("hc", "NotonlydidthecultivatorsurnamedMinappearfearfulbutthegauntoldmanandthefiercelookingmanwerealsofilledwithtrepidationnotknowingwhetherornotthosewordswouldangertheyouthbeforethemTheywerecompletelyunsureaboutwhetherornotthispersonwastheInsectDevilInterestingitseemsthisInsectDevilisquitenotoriousDoyouFellowDaoistsknowtheappearanceoftheInsectDevilorthetypeofinsectsthatheusesNotonlywasHanLinotangrybuthesmiledinsteadCultivatorMinstartedtomumble“WhathelookslikeIveneverheardofthatbeforeItseemshisappearanceisquiteordinaryAsfortheinsectshecontrolstheyshouldbebothgoldandsilverwhenhesaidthisCultivatorMincouldnthelpbutshoutout“YiFellowDaoistcontrolstricoloredbeetlesItseemsSeniortrulyisnttheInsectDevilTheothertwosuddenlyrecalledthisandfelttheirspiritsriseIfthispersontrulywasnttheInsectDevilthentheywouldbefarmorelikelytosurviveHanLithenlookeduptotheskyasifdeepinthoughtAshortmomentlaterheloweredhisheadandsaid“ManythankstoFellowDaoistsfortellingmethetruthSinceIstillhavematterstoattendtoIcantstayanyfurtherHoweverIhopeyouwillkeepourencountertodaybetweenourselvesIdontwishtobemistakenastheInsectDevilandbepursuedIhopeyoucanunderstandThethreewerewildlydelightedbyhiswordsSuppressingtheexcitementinhishearttheoldmanexpectantlyprobed“ThisisonlynaturalWewilldefinitelykeepourmouthsshutaboutthisandwontcauseanyproblemsforyouWellthenusbrotherswillnowbetakingourleaveHanLinoddedwithafaintsmileandthethreeimmediatelysalutedHanLiwithconcealedjoyTheythenhastilystoodupandflewawayAmomentlaterontheothersideoftheislandthethreebroughtalongtheirdisciplesinanimpatientrushtogetawayfromtheislandAtanunknowntimeHanListoodupandremainedstillashewatchedthemflyoffAftertheydisappearedHanLisfacesuddenlybecamesullenAlthoughexterminatingthewholegroupofcultivatorswouldvebeenaneasytaskHanLihadnointerestinattackingthemHewasntthebloodthirtysortafterallBesidesitwouldnthavemademuchofadifferencewhetherornothiswhereaboutswereleakedThislocationwasextremelyfarawayfromhiscaveresidenceHadheencounteredthethreenearthemistyislandhedefinitelywouldnthaveletthemgoInadditionhehadalreadymadeplanstohastilyreturntohiscaveresidenceandenterseclusionforatleastthirtyyearsHedidntwanttowastetimeoutintheOuterStarSeaswhiletherewerepeopleinpursuitofhimHoweveritseemstheyhadgivenhimquitethenefariousnameoftheInsectDevilTherewasatimewherehehadfoundhimselfinahelplesspositionandwasforcedtounleashedhisGoldDevourBeetlestokilltheJadeCloudSectcultivatorsbuttherewasneveranoccurrencewherehehadkilledotherstoseizetheirtreasuresSomeonewasclearlyframinghimAlthoughthisdidntcauseHanLitobecomeseethingwithangeritdidverymuchvexhimAftersomethoughthecametotheconclusionthatthiswaslikelythedoingoftheonlyenemyhehadintheOuterStarSeastheJadeCloudSectDuringthetimewhenHanLiwasstillfearfulofhighgradedemonbeastsandhadtoyetstraytoodeeplyintotheOuterStarSeashehadusedtheRainbowSkirtGrasstocontinuouslylureindemonbeastsandslaythemfortheircoresAsaresulthemanagedtolureinagradesevendemonbeastJustasthishappenedagroupofnineCoreFormationcultivatorsranintohimTheyarrogantlyproclaimedthemselvesastheJadeCloudSectandthoughttogiveintotheiravariceandslayhimforhistreasureAssuchHanLicouldonlyreleasehismanyGoldDevouringBeetlestokillthemandprotecthimselfAlthoughhenaturallythoughtitwouldbebesttokillthemallafterreachingthatpointhedidntexpectthatthelateCoreFormationcultivatoramongthemactuallypossessedanancientprotectivetreasureofimpressivestrengthAsaresulthealonehadmanagedtoescapetheGoldDevouringBeetlescatchingHanLioffguardAsHanLiknewthattheJadeCloudSectwasoneofthegreatpowersofWondrousDepthsIslandhecouldonlybravethedangersofheadingintothefarreachesoftheseatoavoidanypowerfulenemiesthatsoughthimoutItcouldbesaidthatHanLihadbeenquiteluckyIntheseveralyearsthathehadspentinthefarseashehadntencounteredanydemonbeastsofgradeeightorhigherHismostdangerousencounterhadbeenwhenheattractedseveralgradesevendemonbeastsatonceAlthoughthesituationhadlefthimatalossthesimultaneousreleaseofhisGoldDevouringBeetlesandmagictreasuresmanagedtosettletheproblemwithoutmuchtroubleInhishuntingduringthesepastyearsheeventuallyacquiredseveralhundredgradesixandsevendemonbeastcoresmorethanenoughforhismedicinalrecipesAdditionallyhealsoaccumulatedalargecollectionofdemonbeastmaterialsAssuchhefeltsatisfiedwithendinghisexpeditionandreturningbacktohiscaveresidenceHoweverjustashereturnedfromthedeepseasheunintentionallydiscoveredaVividGlassBeastashepassedbythesewatersHanLididntintendonlettingitslipawayandplaceddownaformationtotrapitHoweverhedidntexpectthatthiswouldattractthegauntoldmanandhistwocompanionsTheyevencalledhim‘InsectDemoninapanickedmannerThiscausedHanLismoodtotakeaturnfortheworseItwasmorethanlikelythatsincetheJadeCloudSectwasunabletofindhimtheyhadincitedrumorsofan‘InsectDevilusinghislikenessandpenchantforcontrollinginsectsandhisBambooCloudswarmSwordsItwasclearthattheyhadintendedtodestroyhisreputationanddenyhimanyplaceintheOuterStarSeasforcinghimtoappearTheyevensentpeopletoimpersonatehimandslayothercultivatorsfortheirtreasuresintheprocessmanagingtokilltwobirdswithonestoneHowevertherewasstillsomethingthatHanLicouldntwraphismindaroundItwasntdifficulttofindhighgradecultivatorsthatwereskilledincontrollinginsectsFindingflyinginsectsthatappearedsimilartoGoldDevouringBeetlesalsowasntparticularlydifficultButifthiswastrulythefaultoftheJadeCloudSectwhydidtheimpersonatorsusegoldandsilverinsectsHehadusedhisblacktaintedGoldDevouringBeetlestokilltheJadeCloudSectThelonecultivatorthathadescapeddefinitelywouldnthavemadesuchamistakeHoweverthechangeincolorforhisGoldDevouringBeetleswassomethingthathadonlyoccurredafterhehadarrivedintheOuterStarSeasCoulditbetheoldeccentricsfromHeavenvoidHallhadtrackedhimdownhereWhenHanLicarefullyconsideredithefelthishearttrembleHiscomplexionunconsciouslypaledIfthisweretruethesituationwouldbefarfromgoodAfterstandingstillforamomentmoreandcalmlymutteringtohimselfHanLisuddenlystampedhisfootdownandshottowardstheskySoonafterhestreakedacrosstheskyinazurelightheadingtowardsthedirectionofhissmallislandinthemistAsHanLiflewheworehisordinaryexpressionapartfromacoldsneerthatappearedonhismouthJustnowhehadcometoanunderstandingRegardlessofwhetherthiswastheresultofthemachinationsoftheJadeCloudSectortheNascentSouleccentricstherewasnopointinspendingtoomuchthoughtonthematterofthe‘InsectDevilThiswasbecausewiththedevelopmentofthestrangesituationoftheWondrousDepthshisoriginalplanofprolongedsecludedcultivationwasnowevenmoreadvantageousThiscourseofactionwouldallowhimtoavoidboththelurkingandtheupcomingdangersintheOuterStarSeasAndafterheincreasedhiscultivationwhowoulddaretoapprehendhimevenifhisnotoriousreputationremainedInthecultivationworldstrengthalwaysspoketheloudestWiththatinmindHanLicontinuedonhiswaywithoutevenasliverofhesitationremaininginhisheartMeanwhileinBlackrockCitythereweretwopeopleinahiddenroomspeakingtoeachotherinamysteriousmanner“BrotherQiithasalreadybeenthreeyearsYourmethodshavebeenineffectiveIamnotgoingtowasteanothereightyearsjustforthatyoungstertotakethebaitTheclearvoicespokewithatoneofclearimpatience“FellowDaoistWuyoucantbehastywiththesemattersDontyoualsosweepyourspiritualsenseovereverycornerofBlackrockCitydayafterdayIfthatpersonactuallyappearedinthecitywithadisguisehedefinitelywouldnthavebeenabletoslippastBrotherWuseyesTheotherpersonspokewithahoarseanddeepvoiceThefirstpersonwhospokewasastonishinglyZenithYinwhohadntbeenseenforyearsHewasspeakingtoapalemiddleagedmanwithasullenexpressionHeappeareddissatisfied“HumphDoesBrotherQismethodofsendingdisciplestomasqueradeastheyoungsterrobbingothersserveanotherpurposeBrotherQidoesnthaveanotherpurposeinmindthatheisdeliberatelyhidingfrommeIcantbelievethatfindingasingleearlyCoreFormationcultivatorcouldbesohardforasectaslargeasyourJadeCloudSectZenithYinsaidwithanannoyedexpression“SighBrotherWuswordswrongmeWewerentfriendsforonlyoneortwoyearsHowcouldIpossiblydothatMoreoveroursectalsoholdsadeepenmitywithhimWeveneverstoppedtryingtofindhimTheownerofthehoarsevoicewasamiddleagedDaoistpriestwearingarobeadornedwithwhitecranesHisfacehadwhitepockmarksandwascoveredinalayerofwarmfluorescencemakingforquiteanimposingvisageHethensmiledasifhehadthoughtofsomethingandsaid“HoweverFellowDaoistWuIamquitecuriousJustwhatdidtheyoungsterdotocauseyoutobravetheriskofsneakingintoHeavenlyStarCityandteleportinghereFellowDaoistWuhasalwaysusedhisgrandsonsdeathasanexcuseHoweveritwasalwaysstatedsocasuallythatImverymuchindoubt", "e")
print(encriptado)
desencriptado = traduciMensaje("hola", encriptado, "d")