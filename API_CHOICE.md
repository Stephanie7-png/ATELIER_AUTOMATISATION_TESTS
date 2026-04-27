# API Choice

- Étudiant : stephanie kanga makeu
- API choisie : ipify
- URL base : https://api.ipify.org
- Documentation officielle / README :  https://api.ipify.org
- Auth : None 
- Endpoints testés :
 -GET https://api.ipify.org?format=json
 -GET https://api.ipify.org/?format=json

- Hypothèses de contrat (champs attendus, types, codes) :
 -Code HTTP attendu : 200
 -Format attendu : JSON
 -Champ attendu : ip
 -Type attendu : string
 -Le endpoint retourne l’adresse IP publique du client
 -La réponse doit contenir une IP valide

- Limites / rate limiting connu :
 - Aucune authentification requise
 -Aucune limite stricte publiquement documentée
 -Tests limités à un rythme raisonnable pour éviter la surcharge
- Risques (instabilité, downtime, CORS, etc.) :
 -API publique externe donc possible indisponibilité temporaire
 -Possible lenteur réseau selon la localisation
 -Dépendance à un service tiers
 -Changement futur du format de réponse possible
