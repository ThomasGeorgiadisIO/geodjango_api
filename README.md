# geodjango_api
A JSON REST API with CRUD operations for:

Provider (name, email, phone number, language and currency) at http://localhost:8000/api/provider/

ServiceArea (name, price, geojson information) at http://localhost:8000/api/service_area/

http://localhost:8000/api/check_availability/{lat}/{lng} endpoint that takes a lat/lng pair as arguments and return a list of all polygons that include the given lat/lng. The name of the polygon, provider's name, and price is be returned for each polygon.

## HOW TO RUN

git clone https://github.com/ThomasGeorgiadisIO/geodjango_api.git

cd django_docker/

docker-compose build

docker-compose up -d

 !in case of error! check geodjango_api/django_docker/app/entrypoint.sh encoding. Should be LF and not CRLF.

## DOCUMENTATION
http://localhost:8000/api/schema/redoc/

Documentation auto identifies geojson field as string. It is a PolygonField and accepts geojson like:

{
  type : "Polygon",
  coordinates : [
     [ [ 0 , 0 ] , [ 3 , 6 ] , [ 6 , 1 ] , [ 0 , 0 ] ],
     [ [ 2 , 2 ] , [ 3 , 3 ] , [ 4 , 2 ] , [ 2 , 2 ] ]
  ]
}
